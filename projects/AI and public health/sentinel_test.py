import requests

def check_product_health(product_name):
    # 1. Set up the search parameters
    # We use the v2 search API and ask only for the fields we need to save bandwidth
    url = "https://world.openfoodfacts.org/api/v2/search"
    params = {
        "categories_tags": product_name,
        "fields": "product_name,brands,nova_group,nutriscore_grade,ingredients_text",
        "page_size": 1
    }
    
    # 2. Add a custom User-Agent (Required by Open Food Facts)
    headers = {
        "User-Agent": "GuardianEyeProject/1.0 (contact: your-email@example.com)"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if data['products']:
            product = data['products'][0]
            name = product.get('product_name', 'Unknown')
            brand = product.get('brands', 'Unknown')
            nova = product.get('nova_group', 'N/A')
            nutri = product.get('nutriscore_grade', 'N/A').upper()

            print(f"--- Sentinel Report ---")
            print(f"Product: {name} ({brand})")
            print(f"NOVA Group: {nova} (Level 4 = Ultra-Processed)")
            print(f"Nutri-Score: {nutri}")
            
            if str(nova) == "4":
                print("⚠️ ALERT: This is an Ultra-Processed Food (UPF).")
        else:
            print("No product found.")

    except Exception as e:
        print(f"Error connecting to API: {e}")

# Test the Sentinel logic
check_product_health("Energy Drink")