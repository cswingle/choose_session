library(dplyr)
library(readr)

sessions <- read_csv("sessions")

session_names <- read_csv("session_names")

sessions_with_score <- sessions %>%
    inner_join(session_names) # %>%
    # filter(interest>0)

write_csv(sessions_with_score, "sessions_with_score.csv")
