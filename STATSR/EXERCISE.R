# Exercise 1

# Create a data frame with 5 students
students <- data.frame(
  Name = c("Amit", "Neema", "John", "Sara", "Ravi"),
  Age = c(20, 22, 19, 21, 23),
  Marks = c(85, 67, 45, 78, 92)
)

# View data frame
students

# Find average marks
avg_marks <- mean(students$Marks)
avg_marks

# Find maximum age
max_age <- max(students$Age)
max_age

# Add Grade column based on Marks
students$Grade <- ifelse(students$Marks >= 75, "A",
                         ifelse(students$Marks >= 50, "B", "C"))

# View updated data frame
students



