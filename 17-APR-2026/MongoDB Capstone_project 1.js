//----- Online Store Order Analytics -----

// --- Basic Queries ---

// 1 Display all documents from the customers collection.
db.customers.find()

// 2 Display all documents from the products collection.
db.products.find()

// 3 Display all documents from the orders collection.
db.orders.find()

// 4 Display customers from Hyderabad.
db.customers.find({ city: "Hyderabad" })

// 5 Display products from the Electronics category.
db.products.find({ category: "Electronics" })

// 6 Display orders with status Delivered.
db.orders.find({ status: "Delivered" })


// --- Filtering Queries ---

// 7 Display products whose price is greater than 30000.
db.products.find({ price: { $gt: 30000 } })

// 8 Display products whose price is between 10000 and 50000.
db.products.find({ price: { $gte: 10000, $lte: 50000 } })

// 9 Display customers whose age is greater than 26.
db.customers.find({ age: { $gt: 26 } })

// 10 Display orders whose quantity is greater than 1.
db.orders.find({ quantity: { $gt: 1 } })

// 11 Display products whose stock is less than or equal to 10.
db.products.find({ stock: { $lte: 10 } })

// 12 Display orders whose status is not Cancelled.
db.orders.find({ status: { $ne: "Cancelled" } })

// 13 Display customers from Hyderabad or Mumbai.
db.customers.find({ city: { $in: ["Hyderabad", "Mumbai"] } })


// --- Projection Queries ---

// 14 Display only customer name and city.
db.customers.find({}, { name: 1, city: 1, _id: 0 })

// 15 Display only product name, category, and price.
db.products.find({}, { name: 1, category: 1, price: 1, _id: 0 })

// 16 Display only order_id, quantity, and status.
db.orders.find({}, { order_id: 1, quantity: 1, status: 1, _id: 0 })


// --- Sorting, Limit, Skip ---

// 17 Display products sorted by price ascending.
db.products.find().sort({ price: 1 })

// 18 Display products sorted by price descending.
db.products.find().sort({ price: -1 })

// 19 Display the top 3 most expensive products.
db.products.find().sort({ price: -1 }).limit(3)

// 20 Display the 2 cheapest products.
db.products.find().sort({ price: 1 }).limit(2)

// 21 Skip the first 2 products and display the rest.
db.products.find().skip(2)

// 22 Display customers sorted by age descending.
db.customers.find().sort({ age: -1 })


// --- Update Operations ---

// 23 Update the price of Laptop to 78000.
db.products.updateOne(
  { name: "Laptop" },
  { $set: { price: 78000 } }
)

// 24 Add a new field discount: 10 to all Electronics products.
db.products.updateMany(
  { category: "Electronics" },
  { $set: { discount: 10 } }
)

// 25 Add priority: "High" to orders with status Pending.
db.orders.updateMany(
  { status: "Pending" },
  { $set: { priority: "High" } }
)

// 26 Change Meera’s membership from Bronze to Silver.
db.customers.updateOne(
  { name: "Meera" },
  { $set: { membership: "Silver" } }
)


// --- Delete Operations ---

// 27 Delete the product named Printer.
db.products.deleteOne({ name: "Printer" })

// 28 Delete all products in the Furniture category.
db.products.deleteMany({ category: "Furniture" })

// 29 Delete orders whose status is Cancelled.
db.orders.deleteMany({ status: "Cancelled" })


// --- Count Queries ---

// 30 Count total customers.
db.customers.countDocuments()

// 31 Count products in the Electronics category.
db.products.countDocuments({ category: "Electronics" })

// 32 Count delivered orders.
db.orders.countDocuments({ status: "Delivered" })

// 33 Count customers from Hyderabad.
db.customers.countDocuments({ city: "Hyderabad" })


// --- Aggregation Queries ---

// 34 Find total stock available per category.
db.products.aggregate([
  { $group: { _id: "$category", totalStock: { $sum: "$stock" } } }
])

// 35 Find average product price per category.
db.products.aggregate([
  { $group: { _id: "$category", avgPrice: { $avg: "$price" } } }
])

// 36 Find maximum product price.
db.products.aggregate([
  { $group: { _id: null, maxPrice: { $max: "$price" } } }
])

// 37 Find minimum product price.
db.products.aggregate([
  { $group: { _id: null, minPrice: { $min: "$price" } } }
])

// 38 Calculate total inventory value (price × stock).
db.products.aggregate([
  {
    $group: {
      _id: null,
      totalInventoryValue: { $sum: { $multiply: ["$price", "$stock"] } }
    }
  }
])

// 39 Find total quantity ordered per product.
db.orders.aggregate([
  { $group: { _id: "$product_id", totalQuantity: { $sum: "$quantity" } } }
])

// 40 Find total quantity ordered per customer.
db.orders.aggregate([
  { $group: { _id: "$customer_id", totalQuantity: { $sum: "$quantity" } } }
])


// ---- $lookup queries ----

// 41 Display orders with customer details.
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer_details"
    }
  }
])

// 42 Display orders with product details.
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "product_details"
    }
  }
])

// 43 Display customer name and product name per order.
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "prod"
    }
  },
  { $unwind: "$prod" },
  {
    $project: {
      _id: 0,
      customer_name: "$cust.name",
      product_name: "$prod.name"
    }
  }
])

// 44 Display customer name, city, product name, quantity, and order status.
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "prod"
    }
  },
  { $unwind: "$prod" },
  {
    $project: {
      _id: 0,
      customer_name: "$cust.name",
      city: "$cust.city",
      product_name: "$prod.name",
      quantity: 1,
      status: 1
    }
  }
])