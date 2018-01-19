library("tidyverse")
library("ggplot2")
bdplace <- read.csv("birth_death_places.csv")

# Creates a column with the percentage of people that were born and died in the same place
percentageincluded <- bdplace %>%
  mutate(percentage = birth_death_same/(birth_death_same + birth_death_notsame)*100)
# Plots the development of percentages over time
ggplot()+
  geom_line(data = percentageincluded, mapping = aes(x = year, y = percentage), colour = "red") + labs(x = "Year", y = "Percentage") +
  theme(plot.margin=unit(c(0.5,1,0.5,0.5),"cm"))
# Plots the development of percentages over time as a scatter plot
ggplot()+
  geom_point(data = percentageincluded, mapping = aes(x = year, y = percentage), colour = "red") + labs(x = "Year", y = "Percentage") +
  theme(plot.margin=unit(c(0.5,1,0.5,0.5),"cm"))
