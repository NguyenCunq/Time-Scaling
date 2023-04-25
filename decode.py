import librosa
import numpy as np
import os

def binary_to_text(binary):
   # Chuyển đổi từ chuỗi nhị phân thành chuỗi ký tự với mã ASCII
   return ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])

def read_hidden_message(audio_path):
   # Đọc file âm thanh
   audio, sr = librosa.load(audio_path)

   # Tính toán tỷ lệ thời gian mới so với thời gian gốc
   time_scale_factor = len(audio) / len(audio)

   # Áp dụng phương pháp Time Scaling
   audio_scaled = librosa.effects.time_stretch(audio, time_scale_factor)

   # Đọc file .txt chứa chuỗi nhị phân đã giấu
   binary_message = ''
   with open(audio_path[:-4] + '.txt', 'r') as f:
      binary_message = f.read()

   # Lấy độ dài chuỗi nhị phân từ 8 ký tự đầu tiên của chuỗi
   binary_len = int(binary_message[:8], 2)

   # Tách chuỗi nhị phân thật sự đã giấu từ chuỗi nhị phân còn lại
   binary_message = binary_message[8:binary_len+8]

   # Chuyển đổi chuỗi nhị phân thành đoạn tin đã giấu
   message = binary_to_text(binary_message)

   return message

if __name__ == '__main__':
   # Đường dẫn tới file âm thanh đã giấu tin
   audio_path = 'output.wav'

   # Đọc đoạn tin đã giấu
   hidden_message = read_hidden_message(audio_path)

   # In ra đoạn tin đã giấu
   print(f"The hidden message is: {hidden_message}")
