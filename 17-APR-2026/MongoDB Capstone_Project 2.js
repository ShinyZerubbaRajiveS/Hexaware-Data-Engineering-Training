
// ----- Hospital Appointment & Billing Analytics -----


// --- Basic Queries ---

// 1 Display all documents from the patients collection.
db.patients.find()

// 2 Display all documents from the doctors collection.
db.doctors.find()

// 3 Display all documents from the appointments collection.
db.appointments.find()

// 4 Display patients from Hyderabad.
db.patients.find({ city: "Hyderabad" })

// 5 Display doctors whose specialization is Cardiology.
db.doctors.find({ specialization: "Cardiology" })

// 6 Display appointments whose status is Completed.
db.appointments.find({ status: "Completed" })


// --- Filtering Queries ---

// 7 Display patients whose age is greater than 30.
db.patients.find({ age: { $gt: 30 } })

// 8 Display doctors whose consultation fee is greater than 1000.
db.doctors.find({ consultation_fee: { $gt: 1000 } })

// 9 Display doctors whose consultation fee is between 900 and 1600.
db.doctors.find({ consultation_fee: { $gte: 900, $lte: 1600 } })

// 10 Display appointments whose bill amount is greater than 1000.
db.appointments.find({ bill_amount: { $gt: 1000 } })

// 11 Display appointments whose status is not Cancelled.
db.appointments.find({ status: { $ne: "Cancelled" } })

// 12 Display patients from Hyderabad or Mumbai.
db.patients.find({ city: { $in: ["Hyderabad", "Mumbai"] } })

// 13 Display doctors located in Hyderabad or Delhi.
db.doctors.find({ city: { $in: ["Hyderabad", "Delhi"] } })


// --- Projection Queries ---

// 14 Display only patient name and city.
db.patients.find({}, { name: 1, city: 1, _id: 0 })

// 15 Display only doctor name, specialization, and consultation_fee.
db.doctors.find({}, { name: 1, specialization: 1, consultation_fee: 1, _id: 0 })

// 16 Display only appointment_id, status, and bill_amount.
db.appointments.find({}, { appointment_id: 1, status: 1, bill_amount: 1, _id: 0 })


// --- Sorting, Limit, Skip ---

// 17 Display doctors sorted by consultation_fee ascending.
db.doctors.find().sort({ consultation_fee: 1 })

// 18 Display doctors sorted by consultation_fee descending.
db.doctors.find().sort({ consultation_fee: -1 })

// 19 Display the top 3 highest fee doctors.
db.doctors.find().sort({ consultation_fee: -1 }).limit(3)

// 20 Display the 2 lowest fee doctors.
db.doctors.find().sort({ consultation_fee: 1 }).limit(2)

// 21 Skip the first 2 patients and display the rest.
db.patients.find().skip(2)

// 22 Display patients sorted by age descending.
db.patients.find().sort({ age: -1 })


// --- Update Operations ---

// 23 Update the consultation fee of Dr. Sharma to 1300.
db.doctors.updateOne(
  { name: "Dr. Sharma" },
  { $set: { consultation_fee: 1300 } }
)

// 24 Add a new field priority: "High" to appointments with status Pending.
db.appointments.updateMany(
  { status: "Pending" },
  { $set: { priority: "High" } }
)

// 25 Add a field available: true to doctors located in Hyderabad.
db.doctors.updateMany(
  { city: "Hyderabad" },
  { $set: { available: true } }
)

// 26 Change the city of patient Meera from Chennai to Bangalore.
db.patients.updateOne(
  { name: "Meera" },
  { $set: { city: "Bangalore" } }
)


// --- Delete Operations ---

// 27 Delete the doctor whose name is Dr. Iyer.
db.doctors.deleteOne({ name: "Dr. Iyer" })

// 28 Delete all appointments whose status is Cancelled.
db.appointments.deleteMany({ status: "Cancelled" })

// 29 Delete all patients whose city is Delhi.
db.patients.deleteMany({ city: "Delhi" })


// --- Count Queries ---

// 30 Count total patients.
db.patients.countDocuments()

// 31 Count doctors located in Hyderabad.
db.doctors.countDocuments({ city: "Hyderabad" })

// 32 Count total completed appointments.
db.appointments.countDocuments({ status: "Completed" })

// 33 Count patients from Hyderabad.
db.patients.countDocuments({ city: "Hyderabad" })


// --- Aggregation Queries ---

// 34 Find the average consultation fee per specialization.
db.doctors.aggregate([
  { $group: { _id: "$specialization", avgFee: { $avg: "$consultation_fee" } } }
])

// 35 Find the maximum consultation fee.
db.doctors.aggregate([
  { $group: { _id: null, maxFee: { $max: "$consultation_fee" } } }
])

// 36 Find the minimum consultation fee.
db.doctors.aggregate([
  { $group: { _id: null, minFee: { $min: "$consultation_fee" } } }
])

// 37 Find the total bill amount grouped by appointment status.
db.appointments.aggregate([
  { $group: { _id: "$status", totalBill: { $sum: "$bill_amount" } } }
])

// 38 Find the total appointments handled by each doctor.
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", totalAppointments: { $sum: 1 } } }
])

// 39 Find the total appointments per patient.
db.appointments.aggregate([
  { $group: { _id: "$patient_id", totalAppointments: { $sum: 1 } } }
])

// 40 Find the average patient age per city.
db.patients.aggregate([
  { $group: { _id: "$city", avgAge: { $avg: "$age" } } }
])

// 41 Find the total bill amount generated per doctor.
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", totalBill: { $sum: "$bill_amount" } } }
])

// 42 Find the total bill amount generated per patient city.
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient"
    }
  },
  { $unwind: "$patient" },
  {
    $group: {
      _id: "$patient.city",
      totalBill: { $sum: "$bill_amount" }
    }
  }
])


// --- Multi-Collection Queries using $lookup ---

// 43 Display appointments with patient details.
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_details"
    }
  }
])

// 44 Display appointments with doctor details.
db.appointments.aggregate([
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "doctor_details"
    }
  }
])

// 45 Display patient name and doctor name for each appointment.
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "p"
    }
  },
  { $unwind: "$p" },
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "d"
    }
  },
  { $unwind: "$d" },
  {
    $project: {
      _id: 0,
      patient_name: "$p.name",
      doctor_name: "$d.name"
    }
  }
])

// 46 Display patient name, city, doctor name, specialization, appointment status, and bill amount.
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "p"
    }
  },
  { $unwind: "$p" },
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "d"
    }
  },
  { $unwind: "$d" },
  {
    $project: {
      _id: 0,
      patient_name: "$p.name",
      city: "$p.city",
      doctor_name: "$d.name",
      specialization: "$d.specialization",
      status: 1,
      bill_amount: 1
    }
  }
])

// 47 Display all patients with their appointments.
db.patients.aggregate([
  {
    $lookup: {
      from: "appointments",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "appointments"
    }
  }
])

// 48 Display all doctors with the appointments assigned to them.
db.doctors.aggregate([
  {
    $lookup: {
      from: "appointments",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "appointments"
    }
  }
])


// --- Advanced Aggregation ---

// 49 Find total revenue generated per doctor.
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", totalRevenue: { $sum: "$bill_amount" } } }
])

// 50 Find total revenue generated per specialization.
db.appointments.aggregate([
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "d"
    }
  },
  { $unwind: "$d" },
  {
    $group: {
      _id: "$d.specialization",
      totalRevenue: { $sum: "$bill_amount" }
    }
  }
])

// 51 Find the patient who spent the highest bill amount.
db.appointments.aggregate([
  { $sort: { bill_amount: -1 } },
  { $limit: 1 }
])

// 52 Find the doctor who handled the highest number of appointments.
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", totalAppointments: { $sum: 1 } } },
  { $sort: { totalAppointments: -1 } },
  { $limit: 1 }
])

// 53 Find total revenue generated from completed appointments only.
db.appointments.aggregate([
  { $match: { status: "Completed" } },
  { $group: { _id: null, totalRevenue: { $sum: "$bill_amount" } } }
])

// 54 Find the city with the highest number of appointments.
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "p"
    }
  },
  { $unwind: "$p" },
  { $group: { _id: "$p.city", totalAppointments: { $sum: 1 } } },
  { $sort: { totalAppointments: -1 } },
  { $limit: 1 }
])

// 55 Find the city with the highest bill amount generated.
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "p"
    }
  },
  { $unwind: "$p" },
  { $group: { _id: "$p.city", totalBill: { $sum: "$bill_amount" } } },
  { $sort: { totalBill: -1 } },
  { $limit: 1 }
])

// 56 Find the specialization with the highest average bill amount.
db.appointments.aggregate([
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "d"
    }
  },
  { $unwind: "$d" },
  {
    $group: {
      _id: "$d.specialization",
      avgBill: { $avg: "$bill_amount" }
    }
  },
  { $sort: { avgBill: -1 } },
  { $limit: 1 }
])