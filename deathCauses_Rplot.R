library('tidyverse')
library('ggplot2')
install.packages('ggplot2')

common_deathCauses <- read.csv('common_deathCauses.csv')

# This makes a bar graph of the most common death causes in the years 1820 until 1920
ggplot(common_deathCauses, aes(x = reorder(cause, deaths), y = deaths), position = position_stack(reverse = TRUE)) + coord_flip() + theme(legend.position = "top") +
  geom_bar(stat = "identity", fill = "red") +
  labs(x = "Death Causes", y = "Deaths")
