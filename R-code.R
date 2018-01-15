year_1820 <- read.csv("1820.csv")
year_1920 <- read.csv("1920.csv")

#Now all the information is in this data frames
#1820:
eighteenhundred <- year_1820

eighteenhundred$deathYear <- as.numeric(eighteenhundred$deathYear) 

eighteenhundred$birthYear <- as.numeric(eighteenhundred$birthYear) 

complete18 <- eighteenhundred %>%
  mutate(lifetime = deathYear - birthYear)

#1920:
nineteenhundred <- year_1920

nineteenhundred$deathYear <- as.numeric(nineteenhundred$deathYear) 

nineteenhundred$birthYear <- as.numeric(nineteenhundred$birthYear) 

complete19 <- nineteenhundred %>%
  mutate(lifetime = deathYear - birthYear)