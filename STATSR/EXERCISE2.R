# Exercise 2

# Load iris dataset
data(iris)

# Number of rows and columns
dim(iris)

# First 6 rows
head(iris)

# Mean, median, variance, and standard deviation of Sepal.Length
mean_sepal <- mean(iris$Sepal.Length)
median_sepal <- median(iris$Sepal.Length)
variance_sepal <- var(iris$Sepal.Length)
sd_sepal <- sd(iris$Sepal.Length)

mean_sepal
median_sepal
variance_sepal
sd_sepal

# Number of flowers in each species
table(iris$Species)

# Draw histogram of Petal.Length
hist(iris$Petal.Length,
     main = "Histogram of Petal Length",
     xlab = "Petal Length",
     col = "lightblue",
     border = "black")

# Draw boxplot of Sepal.Width
boxplot(iris$Sepal.Width,
        main = "Boxplot of Sepal Width",
        ylab = "Sepal Width",
        col = "lightgreen")
