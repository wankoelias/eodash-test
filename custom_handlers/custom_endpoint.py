from pystac import Collection, Catalog
from pystac_client import Client


def execute(
    collection: Collection,
    catalog_config: dict,
    endpoint_config: dict,
    collection_config: dict,
):
    if "cerulean" not in catalog_config["title"].lower():
        raise Exception("This demo handler should be run only on cerulean catalog.")
    stac_endpoint_url = endpoint_config["STAC_Url"]
    api = Client.open(stac_endpoint_url)

    # catalog structure is {year}/{year-month}/{year-month-day}/items
    for date_entry in endpoint_config["Subset_Dates"]:
        year, month, day = date_entry.split("-")
        catalog: Catalog = (
            api.get_child(year)
            .get_child(f"{year}-{month}")  # type: ignore
            .get_child(f"{year}-{month}-{day}")  # type: ignore
        )

        for item in catalog.get_items():
            collection.add_item(item)
    return collection
