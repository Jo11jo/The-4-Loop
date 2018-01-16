library("tidyverse")

bdplace <- read.csv("birth_death_places.csv")

# Creates a column with the percentage of people that were born and died in the same place
percentageincluded <- bdplace %>%
  mutate(percentage = birth_death_same/(birth_death_same + birth_death_notsame)*100)
# Plots the development of percentages over time
ggplot()+
  geom_line(data = percentageincluded, mapping = aes(x = year, y = percentage), colour = "red")

