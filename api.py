from vetiver import VetiverModel, VetiverAPI
import pins

b = pins.board_folder("data/model", allow_pickle_read=True)
v = VetiverModel.from_pin(b, "penguin_model")

api = VetiverAPI(v, check_prototype=True)
api.run(port=8080)
