#Glicko Fight Prediction

library(PlayerRatings)

#load glicko ratings
glicko_rating <- readRDS("/glicko_rating/glicko_rating.rds")

#load upcoming fights
ufc_upcoming_file <- list.files("/data/upcoming")
ufc_upcoming_file <- ufc_upcoming_file[grep(".csv$", ufc_upcoming_file)]
ufc_upcoming <- read.csv(paste0("/data/upcoming/", ufc_upcoming_file))[, c("fighter_1", "fighter_2", "fight_id", "date", "location", "weight_class")]

#data prep
colnames(ufc_upcoming)[1] <- "R_fighter"
colnames(ufc_upcoming)[2] <- "B_fighter"

apply(ufc_upcoming, MARGIN = 1, fight_prediction)

fight_prediction_df <- data.frame(date = character(), 
                                  R_fighter = character(), 
                                  B_fighter = character(), 
                                  fight_id = character(), 
                                  location = character(), 
                                  weight_class = character(), 
                                  R_fighter_pred_win_prob = double(), 
                                  B_fighter_pred_win_prob = double())

write.csv(fight_prediction_df, "/fight_prediction/fight_prediction.csv", row.names = FALSE)

fight_prediction <- function(row){
    fight <- row["date", "R_fighter", "B_fighter"]
    fight$date <- as.numeric(fight$date)

    R_fighter_pred_win_prob <- predict(glicko_rating, fight, tng = 1, trat = c(1500, 290))
    B_fighter_pred_win_prob <- predict(glicko_rating, fight[, c(1, 3, 2)], tng = 1, trat = c(1500, 290))

    fight_pred <- cbind(row, R_fighter_pred_win_prob, B_fighter_pred_win_prob)
    rbind(fight_prediction_df, fight_pred)
}