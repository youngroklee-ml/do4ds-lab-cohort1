from vetiver import VetiverModel, VetiverAPI
import pins

b = pins.board_s3("do4ds-lab-letsgo", allow_pickle_read=True)
v = VetiverModel.from_pin(b, "penguin_model", version="20240515T231632Z-d45a2")

api = VetiverAPI(v, check_prototype=True)
api.run(port=8080)
