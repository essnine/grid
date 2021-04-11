class Grid:
    def __init__(self, instance_id) -> None:
        self.instance_id = instance_id
        self.grid_size = [0,0]
        self.grid_active = False
        self.session_params = {
            # default session params will go here,
            # when I figure them out clearly
        }

    def set_grid_size(self, size:int):
        self.grid_size = [size,size]
    
    def grid_init(self):
        self.grid_active = True

    def simulation_parameters(self, params_list:dict):
        if len(params_list) > 0:
            self.session_params = params_list
        pass