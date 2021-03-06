from PIL import Image
from imageOperation import ImageOperation 

class GetHealth:
    def __init__(self, image_path, saved_location_player_one, saved_location_player_two):
        self.image_path = image_path
        self.saved_location_player_one = saved_location_player_one
        self.saved_location_player_two = saved_location_player_two
        # Mehmood laptop
        # self.coordinates_player_two = (1700, 80, 2800,150 )
        # self.coordinates_player_one = (250, 80,1350,150 )
        # Gap PC 
        # self.coordinates_player_two = (1070, 90, 1670,130 )
        # self.coordinates_player_one = (250, 90,850,130 )
        self.coordinates_player_one = (170, 60, 570, 90 )
        self.coordinates_player_two = (710, 60, 1110, 90 )
            

    def capturePlayerOneHealthBar(self):
        image_obj = Image.open(self.image_path)
        cropped_image = image_obj.crop(self.coordinates_player_one)
        image_operation_instance = ImageOperation(cropped_image)
        count = image_operation_instance.thresholdingImage(100)
        cropped_image.save(self.saved_location_player_one)
        return count
        # cropped_image.show()


    def capturePlayerTwoHealthBar(self):
        image_obj = Image.open(self.image_path)
        cropped_image = image_obj.crop(self.coordinates_player_two)
        
        image_operation_instance = ImageOperation(cropped_image)
        count = image_operation_instance.thresholdingImage(100)
        cropped_image.save(self.saved_location_player_two)
        return count
        
        # cropped_image.show()

class States():

    def stateHealthCalculate(self, pre_state):
        #  for i in range(20):
        # print("#############"+str(i+1))
        image_path = "./pictures/tekken-7-4k.png"
        saved_location_player_one = './pictures/cropped-player-one.png'
        saved_location_player_two = './pictures/cropped-player-two.png'
        instance = GetHealth(image_path, saved_location_player_one, saved_location_player_two)
        count1 = instance.capturePlayerOneHealthBar()
        count2 = instance.capturePlayerTwoHealthBar()
        # if i == 0:
        max1 = 3000
        max2 = 3000
        # print(count1)
        # print(count2)
        
        if count1 > max1:
            max1 = max2 = count1
        if count2 > max2:
            max1 = max2 = count2

        health_player_one = round((count1 / max1 ) * 100)
        health_player_two = round((count2 / max2) * 100)
        if health_player_two >= pre_state[1]:
            health_player_two = pre_state[1]
        if health_player_one >= pre_state[0]:
            health_player_one = pre_state[0]
        print("health_player_one = ", health_player_one)
        print("health_player_two = ", health_player_two)

        return [health_player_one,health_player_two]

    def stateTimeCalculate(self):

        return 60

if __name__ == '__main__':


    state = States()
    state.stateHealthCalculate()
    state.stateTimeCalculate()






