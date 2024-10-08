extends Resource
class_name ProductList

@export var products: Array[Dictionary] = []

func get_product(id: int) -> Dictionary:
	for product in products:
		if product.product_id == id:
			return product
	return {}
