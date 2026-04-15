
// 1. Display all members
db.members.find()

// 2. Display all books
db.books.find()

// 3. Display all borrowings
db.borrowings.find()



// 4. Members from Hyderabad
db.members.find({ city: "Hyderabad" })

// 5. Books in Database category
db.books.find({ category: "Database" })

// 6. Books with price > 600
db.books.find({ price: { $gt: 600 } })

// 7. Borrowings with days_borrowed > 5
db.borrowings.find({ days_borrowed: { $gt: 5 } })



// 8. Books sorted by price descending
db.books.find().sort({ price: -1 })

// 9. Members sorted by name ascending
db.members.find().sort({ name: 1 })



// 10. Total members
db.members.countDocuments()

// 11. Total books
db.books.countDocuments()

// 12. Books in Database category
db.books.countDocuments({ category: "Database" })



// 13. Average book price
db.books.aggregate([
  { $group: { _id: null, avgPrice: { $avg: "$price" } } }
])

// 14. Maximum book price
db.books.aggregate([
  { $group: { _id: null, maxPrice: { $max: "$price" } } }
])

// 15. Minimum book price
db.books.aggregate([
  { $group: { _id: null, minPrice: { $min: "$price" } } }
])

// 16. Total days borrowed per member
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_days: { $sum: "$days_borrowed" }
    }
  }
])



// 17. Borrowings with member details
db.borrowings.aggregate([
  {
    $lookup: {
      from: "members",
      localField: "member_id",
      foreignField: "member_id",
      as: "member_info"
    }
  }
])

// 18. Borrowings with book details
db.borrowings.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book_info"
    }
  }
])

// 19. Member name and book title
db.borrowings.aggregate([
  {
    $lookup: {
      from: "members",
      localField: "member_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  { $unwind: "$member" },
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  {
    $project: {
      _id: 0,
      member_name: "$member.name",
      book_title: "$book.title"
    }
  }
])

// 20. Book title and total times borrowed
db.borrowings.aggregate([
  {
    $group: {
      _id: "$book_id",
      total_borrowed: { $sum: 1 }
    }
  },
  {
    $lookup: {
      from: "books",
      localField: "_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  {
    $project: {
      _id: 0,
      book_title: "$book.title",
      total_borrowed: 1
    }
  }
])



// 21. Total books borrowed by each member
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_books: { $sum: 1 }
    }
  }
])

// 22. Most borrowed book
db.borrowings.aggregate([
  {
    $group: {
      _id: "$book_id",
      total: { $sum: 1 }
    }
  },
  { $sort: { total: -1 } },
  { $limit: 1 }
])

// 23. Total borrowing count by category
db.borrowings.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  {
    $group: {
      _id: "$book.category",
      total_borrowed: { $sum: 1 }
    }
  }
])

// 24. Members who borrowed more than one book
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total: { $sum: 1 }
    }
  },
  { $match: { total: { $gt: 1 } } }
])



// 25. Member name, city, total books borrowed (sorted)
db.borrowings.aggregate([
  {
    $group: {
      _id: "$member_id",
      total_books: { $sum: 1 }
    }
  },
  {
    $lookup: {
      from: "members",
      localField: "_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  { $unwind: "$member" },
  {
    $project: {
      _id: 0,
      name: "$member.name",
      city: "$member.city",
      total_books: 1
    }
  },
  { $sort: { total_books: -1 } }
])