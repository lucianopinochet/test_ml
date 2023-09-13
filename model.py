import csv
def main():
  limits_field = [[0,0,0,0]for _ in range(10)]
  with open("heart_model.csv","r") as model_file:
    csv_reader = csv.reader(model_file)
    for index, line in enumerate(csv_reader):
      if index>0:
        limits_field[index-1][0] = float(line[0])
        limits_field[index-1][1] = float(line[1])
        limits_field[index-1][2] = float(line[2])
        limits_field[index-1][3] = float(line[3])
  with open("heart.csv", "r") as data_file:
    csv_reader  = csv.reader(data_file)
    for index_file, line in enumerate(csv_reader):
      if index_file > 0:
        for index_line, field in enumerate(line[:10]):
          if int(line[10]) == 1:
            limits_field[index_line][0] = limits_field[index_line][0] +   float(field)
            limits_field[index_line][2] = limits_field[index_line][2] +   1
          else:
            limits_field[index_line][1] = limits_field[index_line][1] +   float(field)
            limits_field[index_line][3] = limits_field[index_line][3] +   1
  max_min = []
  with open("heart_model.csv", "w", newline='') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["total_max","total_min","divisor_max","divisor_min"])
    for row in limits_field:
      csv_file.writerow([row[0],row[1],row[2],row[3]])
    for line in limits_field:
      max_model =  line[0]/line[2]
      min_model = line[1]/line[3]
      max_min.append([max_model,min_model])
      # print(max_model, min_model)
  with open("heart.csv", "r") as file:
    rdr = csv.reader(file)
    for index_line, line in enumerate(rdr):
      total = 0
      if index_line > 0:
        for index_field, field_value in enumerate(line[:10]):
          max_value, min_value = max_min[index_field]
          if max_value > min_value:
            reminder = max_value - min_value
            if float(field_value) >= max_value:
              total+=10              
            elif float(field_value) > min_value:
              rest = float(field_value) - min_value
              total += (rest/reminder) * 10
          elif max_value < min_value:
            reminder = min_value - max_value
            if float(field_value) >= min_value:
              total+=10              
            elif float(field_value) > max_value:
              rest = float(field_value) - max_value
              total += (rest/reminder) * 10
          else:
            total+=10
          # print(max_value, min_value)
          # break
        if total >= 50:
          if float(line[10]) == 1:
            print("✅")
          else:
            print("⛔")
        else:
          if float(line[10]) == 0:
            print("✅")
          else:
            print("⛔")
main()
  
