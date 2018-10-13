import Algorithmia

image_number = 10

input = {
  "imageUrl": "data://paubric3/protest_data/" + str(image_number) + ".jpg",
  "outputUrl": "data://paubric3/protest_data/" + str(image_number) + "_result.jpg"
}
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('opencv/BodyDetection/1.0.0')
print(algo.pipe(input).result)
