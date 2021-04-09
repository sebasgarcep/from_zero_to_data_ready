import re
from datetime import datetime
import pandas as pd
from src.utils.data import get_data_path

def process_csv_dump(context):
    files = [
        "T-Codigos de barras.csv",
        "T-Lista colores.csv",
        "T-Tipo de prenda.csv",
        "T-Sexo.csv",
        "T-Lista siluetas.csv",
        "T-Lista tallas.csv",
        "T-Datos cliente.csv",
        "T-Factura.csv",
        "T-FacturaOriginal.csv",
        "T-Factura cotizacion.csv",
        "T-Factura cotizacion2.csv",
        "T-Vendedoras.csv",
        "T-Inventario.csv",
        "T-Inventario dañado.csv",
        "T-Ventas.csv",
        "T-Ventas1.csv",
        "T-Cotizaciones.csv",
        "T-CotizacionesOriginal.csv",
        "T-Formas de pago.csv",
        "T-Formas de pago Cotizaciones.csv",
    ]

    context.environment.create_blank_directory(context.bucket_names.csv_bucket)
    for item in files:
        context.cloud.download_file(context.bucket_names.csv_bucket, item)

    # barcodes
    barcodes = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Codigos de barras.csv"))
    barcodes = barcodes[["Codigo de barras", "Referencia", "Tipo prenda", "Sexo", "Silueta", "Color", "Talla"]]
    barcodes = barcodes.rename(columns = {
        "Codigo de barras": "barcode",
        "Referencia": "reference",
        "Tipo prenda": "clothing_type_id",
        "Sexo": "gender_id",
        "Silueta": "silhouette_id",
        "Color": "color_id",
        "Talla": "size_id"
    })
    context.warehouse.upload_dataframe("staging", "barcodes", barcodes)

    # colors
    colors = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Lista colores.csv"))
    colors = colors.rename(columns = { "Color": "description", "#Color": "id" })
    context.warehouse.upload_dataframe("staging", "colors", colors)

    # clothing types
    clothing_types = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Tipo de prenda.csv"))
    clothing_types = clothing_types.rename(columns = { "Tipo de prenda": "description", "id tipo de prenda": "id" })
    context.warehouse.upload_dataframe("staging", "clothing_types", clothing_types)

    # genders
    genders = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Sexo.csv"))
    genders = genders.rename(columns = { "Sexo": "description", "Id sexo": "id" })
    context.warehouse.upload_dataframe("staging", "genders", genders)

    # silhouettes
    silhouettes = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Lista siluetas.csv"))
    silhouettes = silhouettes.rename(columns = { "Silueta": "description", "id silueta": "id" })
    context.warehouse.upload_dataframe("staging", "silhouettes", silhouettes)

    # sizes
    sizes = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Lista tallas.csv"))
    sizes = sizes.rename(columns = { "Talla": "id" })
    context.warehouse.upload_dataframe("staging", "sizes", sizes)

    # inventory
    mint_inventory = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Inventario.csv"))
    mint_inventory = mint_inventory[["Codigo de barras", "Inventario"]]
    mint_inventory = mint_inventory.rename(columns = {"Codigo de barras": "barcode", "Inventario": "quantity" })
    mint_inventory = mint_inventory[mint_inventory["quantity"] > 0]
    mint_inventory = mint_inventory.groupby("barcode")[["quantity"]].max().reset_index()

    damaged_inventory = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Inventario dañado.csv"))
    damaged_inventory = damaged_inventory.rename(columns = { "Codigo de barras": "barcode", "Dañado": "damaged" })
    damaged_inventory = damaged_inventory.groupby("barcode")[["damaged"]].max().reset_index()

    inventory = mint_inventory.merge(damaged_inventory, on = "barcode", how = "outer")
    inventory["quantity"] = inventory["quantity"].fillna(0)
    inventory["damaged"] = inventory["damaged"].fillna(0)

    context.warehouse.upload_dataframe("staging", "inventory", inventory)

    # clients
    clients = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Datos cliente.csv"))
    clients = clients[clients["Cedula"] == clients["Cedula"].round()]
    clients["Nombre"] = clients["Nombre"].str.upper() + " " +  clients["Segundo apellido"].str.upper()

    email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    def email_parser(text):
        if text == "" or not re.search(email_regex, text):
            return None
        return text
    clients["Email"] = clients["Referencia"].fillna("").apply(email_parser)

    clients["Nombre"] = clients["Nombre"]
    clients["Direccion"] = clients["Direccion"]
    clients["Ciudad"] = clients["Ciudad"]
    clients["Telefono casa num"] = clients["Telefono casa num"].fillna(0).astype("int64")
    clients["Telefono casa"] = clients["Telefono casa"].astype("float").apply(lambda x: x if x < 10**10 else 0).astype("int64")
    clients["Telefono casa"] = clients.apply(lambda row: row["Telefono casa"] if row["Telefono casa"] != 0 else row["Telefono casa num"], axis = 1)
    clients["Telefono casa"] = clients["Telefono casa"].astype("string").apply(lambda x: x if x != "0" else None)
    clients["Telefono trabajo"] = clients["Telefono trabajo"].fillna(0).astype("int64").astype("string").apply(lambda x: x if x != "0" else None)
    clients["Telefono celular"] = clients["Telefono celular"].fillna(0).astype("int64").astype("string").apply(lambda x: x if x != "0" else None)
    clients["Barrio"] = clients["Barrio"]

    birthday_regex = "^\d\d/\d\d/\d\d\d\d$"
    birthday_format = "%d/%m/%Y"
    def birthday_parser(text):
        if text == "" or not re.search(birthday_regex, text):
            return None
        return datetime.strptime(text, birthday_format)
    clients["Cumpleaños"] = clients["Cumpleaños"].fillna("").apply(birthday_parser)

    clients = clients[["Nombre", "Cedula", "Direccion", "Ciudad", "Email",
        "Telefono trabajo", "Telefono celular", "Barrio", "Cumpleaños", "Telefono casa"]]
    clients = clients.rename(columns = { "Nombre": "name", "Cedula": "id", "Direccion": "address",
        "Ciudad": "city", "Telefono casa num": "home_phone", "Email": "email", "Telefono trabajo": "work_phone",
        "Telefono celular": "cellphone", "Barrio": "neighborhood", "Cumpleaños": "birthday",
        "Telefono casa": "home_phone" })

    context.warehouse.upload_dataframe("staging", "clients", clients)

    # salespersons
    salespersons = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Vendedoras.csv"))
    salespersons = salespersons.rename(columns = { "Vendedora": "id" })
    context.warehouse.upload_dataframe("staging", "salespersons", salespersons)

    # invoices
    # Venta
    columns = ["Factura #", "Fecha Venta", "Vendedora", "Cedula", "hora"]
    mapping = { "Factura #": "id", "Fecha Venta": "date",  "Vendedora": "salesperson_id", "Cedula": "client_id", "hora": "time" }
    invoices_1 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Factura.csv"))
    invoices_2 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-FacturaOriginal.csv"))
    invoices_1 = invoices_1[columns]
    invoices_2 = invoices_2[columns]
    invoices_1 = invoices_1.rename(columns = mapping)
    invoices_2 = invoices_2.rename(columns = mapping)
    # Cotizaciones
    columns = ["cFactura #", "Fecha Venta", "Vendedora", "Cedula", "hora"]
    mapping = { "cFactura #": "id", "Fecha Venta": "date", "Vendedora": "salesperson_id", "Cedula": "client_id", "hora": "time" }
    invoices_3 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Factura cotizacion.csv"))
    invoices_4 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Factura cotizacion2.csv"))
    invoices_3 = invoices_3[columns]
    invoices_4 = invoices_4[columns]
    invoices_3 = invoices_3.rename(columns = mapping)
    invoices_4 = invoices_4.rename(columns = mapping)
    # Join
    invoices = pd.concat([invoices_1, invoices_2, invoices_3, invoices_4])
    invoices["id"] = invoices["id"].astype("int64")
    # Clean date
    invoices["date"] = pd.to_datetime(invoices["date"], format = "%m/%d/%y 00:00:00")
    # Clean time
    dirty_times = invoices["time"].notnull() \
        & ~invoices["time"].fillna("").str.endswith("p.m.") \
        & ~invoices["time"].fillna("").str.endswith("a.m.") \
        & ~invoices["time"].fillna("").str.match("^\d\d:\d\d$") \
        & ~invoices["time"].fillna("").str.match("^\d\d:\d\d $") \
        & ~invoices["time"].fillna("").str.endswith("a. m.") \
        & ~invoices["time"].fillna("").str.endswith("p. m.")
    invoices.loc[dirty_times, "time"] = None
    invoices["time"] = invoices["time"].fillna("12:00 AM")
    invoices["time"] = invoices["time"].str.replace("a.m.", "AM", regex = False)
    invoices["time"] = invoices["time"].str.replace("p.m.", "PM", regex = False)
    invoices["time"] = invoices["time"].str.replace("a. m.", "AM", regex = False)
    invoices["time"] = invoices["time"].str.replace("p. m.", "PM", regex = False)
    def add_period(x):
        x = x.strip()
        if not x.endswith("AM") and not x.endswith("PM"):
            v = int(x[0:2])
            return x + " AM" if v < 12 else x + " PM"
        else:
            return x
    invoices["time"] = invoices["time"].apply(add_period)
    invoices["time"] = invoices["time"].apply(lambda x: datetime.strptime(x, "%I:%M %p"))
    invoices["time"] = invoices["time"].apply(lambda x: x.strftime("%H:%M:00"))
    invoices["client_id"] = invoices["client_id"].round()
    invoices["client_id"] = invoices["client_id"].apply(lambda x: x if x != 0 else None)
    invoices = invoices.groupby(["id", "date"])[["salesperson_id", "client_id", "time"]].first().reset_index()
    context.warehouse.upload_dataframe("staging", "invoices", invoices)

    # sales
    columns = ["# factura", "Fecha venta", "Codigo de barras", "% Descuento", "Descuento", "Precio venta fijo"]
    mapping = { "# factura": "invoice_id", "Fecha venta": "invoice_date", "Codigo de barras": "barcode", "% Descuento": "discount_percentage", "Descuento": "discount", "Precio venta fijo": "price" }
    # Read CSVs
    sales_1 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Ventas.csv"))
    sales_2 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Ventas1.csv"))
    sales_3 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Cotizaciones.csv"))
    sales_4 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-CotizacionesOriginal.csv"))
    # Get Columns
    sales_1 = sales_1[columns]
    sales_2 = sales_2[columns]
    sales_3["Precio venta fijo"] = sales_3["Precio venta Fijo"]
    sales_3 = sales_3[columns]
    sales_4["Precio venta fijo"] = sales_4["Precio venta Fijo"]
    sales_4 = sales_4[columns]
    # Rename columns
    sales_1 = sales_1.rename(columns = mapping)
    sales_2 = sales_2.rename(columns = mapping)
    sales_3 = sales_3.rename(columns = mapping)
    sales_4 = sales_4.rename(columns = mapping)
    # Join parts
    sales = pd.concat([sales_1, sales_2, sales_3, sales_4])
    sales = sales.reset_index(drop = True)
    # Clean barcodes
    sales = sales[sales["barcode"].notnull()]
    # Clean sales price
    sales = sales[sales["price"].notnull()]
    # Clean discount_percentage
    sales["discount_percentage"] = sales["discount_percentage"].fillna(0)
    sales["discount_percentage"] = sales["discount_percentage"].apply(lambda x: x / 100.0 if x >= 1 else x)
    # Clean discount
    sales["discount"] = sales["discount"].fillna(0)
    # Merge discount_percentage and discount
    tmp1 = sales[sales["discount"] != 0].groupby("invoice_id")[["price"]].sum()
    tmp2 = sales[sales["discount"] != 0].groupby("invoice_id")[["discount"]].max()
    sales["discount_percentage_2"] = tmp2["discount"] / tmp1["price"]
    sales["discount_percentage_2"] = sales["discount_percentage_2"].fillna(0)
    sales["discount_percentage"] = sales.apply(lambda row: row["discount_percentage"] if row["discount_percentage"] != 0 else row["discount_percentage_2"], axis = 1)
    sales = sales.drop(["discount", "discount_percentage_2"], axis = 1)
    sales = sales[sales["invoice_id"].notnull()]
    sales["invoice_id"] = sales["invoice_id"].astype("int64")
    sales["price"] = sales["price"].astype("int64")
    # Clean date
    sales["invoice_date"] = pd.to_datetime(sales["invoice_date"], format = "%m/%d/%y 00:00:00")
    context.warehouse.upload_dataframe("staging", "sales", sales)

    # payments
    payments_1 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Formas de pago.csv"))
    payments_1 = payments_1[["Factura #", "Fecha", "Tipo de pago", "Cantidad"]]
    payments_1 = payments_1.rename(columns = { "Factura #": "invoice_id", "Fecha": "invoice_date", "Tipo de pago": "type", "Cantidad": "amount" })

    payments_2 = pd.read_csv(get_data_path(context.bucket_names.csv_bucket, "T-Formas de pago Cotizaciones.csv"))
    payments_2 = payments_2[["Cfactura #", "Fecha", "Tipo de pago", "Cantidad"]]
    payments_2 = payments_2.rename(columns = { "Cfactura #": "invoice_id", "Fecha": "invoice_date", "Tipo de pago": "type", "Cantidad": "amount" })

    payments = pd.concat([payments_1, payments_2])
    # Clean data
    payments["invoice_date"] = pd.to_datetime(payments["invoice_date"], format = "%m/%d/%y 00:00:00")
    payments["invoice_id"] = payments["invoice_id"].astype("int64")
    payments = payments[payments["amount"].notnull()]
    payments["amount"] = payments["amount"].astype("int64")
    context.warehouse.upload_dataframe("staging", "payments", payments)