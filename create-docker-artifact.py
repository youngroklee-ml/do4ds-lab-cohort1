import vetiver
import pins
b = pins.board_folder('data/model', allow_pickle_read=True)
v = vetiver.VetiverModel.from_pin(b, 'penguin_model')
vetiver.write_app(board=b, pin_name='penguin_model', file='docker/app.py', overwrite=True)
vetiver.load_pkgs(v, path='docker/vetiver_', packages=vetiver.get_board_pkgs(b))
vetiver.write_docker(app_file='app.py', path='docker/')
