while True:
  description = input("How do you feel right now?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("It's alright, you'll feel better soon, but for now grab a donut and listen to music. ")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("That's great :D ! ")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("Life tires you out, take a break then pick yourself up and move on. You're strong enough :D")
      counter += 1
      patch-1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("Finish what you have to do and enjoy yourselves later")
      counter += 1

 main
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("I hope you find something new to do!")
      counter += 1
      
 main

    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("Breathe in breathe out relax. Don't say anything first")
      counter += 1
    if each_word == "confused":
      feelings_list.append("confused")
      encouragement_list.append("Ask your friend or someone for help")
      counter += 1
 main
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you have a great day! :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
