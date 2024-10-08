extends Resource
class_name IndustryList

@export var industries: Array[Dictionary] = []

func get_industry(id: int) -> Dictionary:
	for industry in industries:
		if industry.industry_id == id:
			return industry
	return {}

func get_industry_products(id: int) -> ProductList:
	var industry = get_industry(id)
	if industry.has("products_resource"):
		return load(industry.products_resource)
	return null