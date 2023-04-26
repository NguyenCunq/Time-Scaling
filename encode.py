import librosa
import numpy as np
import os
import soundfile as sf


def binary_to_text(binary):
   # Chuyển đổi từ chuỗi nhị phân thành chuỗi ký tự với mã ASCII
   return ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])


def text_to_binary(text):
   # Chuyển đổi từ chuỗi ký tự thành chuỗi nhị phân với mã ASCII
   return ''.join([format(ord(char), '08b') for char in text])


def hide_message(audio_path, message, output_path):
   # Đọc file âm thanh
   audio, sr = librosa.load(audio_path)

   # Chuyển đổi đoạn tin cần giấu thành chuỗi nhị phân
   binary_message = text_to_binary(message)

   # Tính toán tỷ lệ thời gian mới so với thời gian gốc
   time_scale_factor = 1.0 + len(binary_message) / len(audio)

   # Áp dụng phương pháp Time Scaling
   audio_scaled = librosa.effects.time_stretch(audio, time_scale_factor)

   # Chuyển đổi dữ liệu âm thanh thành số thực để có thể lưu vào file .wav
   audio_scaled = audio_scaled.astype(np.float32)

   # Ghi file âm thanh mới
   sf.write('output.wav', audio_scaled, sr, subtype='FLOAT')

   # Thêm độ dài chuỗi nhị phân vào đầu chuỗi để tách tin
   binary_message = f"{len(binary_message):08b}" + binary_message

   # Lưu chuỗi nhị phân vào file .txt
   with open(output_path[:-4] + '.txt', 'w') as f:
      f.write(binary_message)


if __name__ == '__main__':
   # Đường dẫn tới file âm thanh gốc
   audio_path = 'input.wav'

   # Đoạn tin cần giấu
   message = 'b19dcat015'

   # Đường dẫn tới file âm thanh mới chứa tin giấu
   output_path = 'output.wav'

   # Giấu tin vào file âm thanh
   hide_message(audio_path, message, output_path)

   print(f"Da giau tin '{message}' vao file am thanh '{audio_path}' va luu ket qua vao file '{output_path}'")

