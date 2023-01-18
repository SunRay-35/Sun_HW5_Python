# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file_obj_1 = open('text_to_encode.txt', 'r')
file_obj_2 = open('text_to_decode.txt', 'r')
text_to_encode = file_obj_1.readline()
text_to_decode = file_obj_2.readline()
file_obj_1.close()
file_obj_2.close()

def encode_text(text):
    count = 0
    result = ''
    for i in range(len(text)):
        if count == 0:
            temp = text[i]
            count += 1
        elif text[i] == temp:
            count +=1    
        else:
            result += str(count) + temp
            temp = text[i]
            count = 1
        if i == len(text)-1:
                result += str(count) + temp
    return result

def decode_text(text):
    result = ''
    for i in range(0,len(text),2):
        count = int(text[i])
        temp = text[i+1]
        while count > 0:
            result += temp
            count -= 1
    return result


encoded_text = encode_text(text_to_encode)
decoded_text = decode_text(text_to_decode)

print(f'Текст {text_to_encode} будет зашифрован как {encoded_text}')
print(f'Текст {text_to_decode} будет расшифрован как {decoded_text}')

file_obj_1 = open('encoded_text.txt', 'w')
file_obj_2 = open('decoded_text.txt', 'w')
file_obj_1.write(encoded_text)
file_obj_2.write(decoded_text)
file_obj_1.close()
file_obj_2.close()