//--> Basic queries
// 1
db.products.find()

// 2
db.products.find({ category: "Electronics" })

// 3
db.products.find({ city: "Hyderabad" })

// 4
db.products.find({ price: { $gt: 30000 } })

// 5
db.products.find({ price: { $lt: 20000 } })

//-->Filtering queries
// 6
db.products.find({ price: { $gte: 10000, $lte: 50000 } })

// 7
db.products.find({ category: "Furniture" })

// 8
db.products.find({ category: "Electronics", city: "Hyderabad" })

// 9
db.products.find({ city: { $in: ["Hyderabad", "Bangalore"] } })

// 10
db.products.find({ category: { $ne: "Furniture" } })

//-->Projection queries
// 11
db.products.find({}, { name: 1, price: 1, _id: 0 })

// 12
db.products.find({}, { name: 1, category: 1, city: 1, _id: 0 })

//-->Sorting queries
// 13
db.products.find().sort({ price: 1 })

// 14
db.products.find().sort({ price: -1 })

//-->Limit Queries
// 15
db.products.find().sort({ price: -1 }).limit(3)

// 16
db.products.find().sort({ price: 1 }).limit(2)

//-->Skip query
// 17
db.products.find().skip(2)

//-->Additional filtering
// 18
db.products.find({ stock: { $gt: 10 } })

// 19
db.products.find({ stock: { $lte: 10 } })

// 20
db.products.find({ category: "Electronics", price: { $gt: 40000 } })

//-->Update operation
// 21
db.products.updateOne(
  { name: "Laptop" },
  { $set: { price: 55000 } } // change value as needed
)

// 22
db.products.updateMany(
  { category: "Electronics" },
  { $set: { discount: 10 } }
)

//-->Delete operation
// 23
db.products.deleteOne({ name: "Printer" })

// 24
db.products.deleteMany({ category: "Furniture" })

//-->Counting Documents
// 25
db.products.countDocuments()

// 26
db.products.countDocuments({ category: "Electronics" })

//-->Aggregation queries
// 27 
db.products.aggregate([
  { $group: { _id: "$category", totalStock: { $sum: "$stock" } } }
])

// 28
db.products.aggregate([
  { $group: { _id: "$category", avgPrice: { $avg: "$price" } } }
])

// 29 
db.products.aggregate([
  { $group: { _id: null, maxPrice: { $max: "$price" } } }
])

// 30 
db.products.aggregate([
  {
    $group: {
      _id: null,
      totalValue: { $sum: { $multiply: ["$price", "$stock"] } }
    }
  }
])