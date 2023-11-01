import subprocess  # Import the subprocess module to run external commands
import numpy  # Import the NumPy library for numerical operations

# EXERCISE 1: RGB to YUV and YUV to RGB conversion functions

def rgb_to_yuv(R, G, B):
    # RGB to YUV conversion
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16  # Calculate the Y component
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128  # Calculate the U component
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128  # Calculate the V component
    return Y, U, V

def yuv_to_rgb(Y, U, V):
    # YUV to RGB conversion
    R = 1.164 * (Y - 16) + 1.596 * (V - 128)  # Calculate the R component
    G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128)  # Calculate the G component
    B = 1.164 * (Y - 16) + 2.018 * (U - 128)  # Calculate the B component
    return R, G, B

# EXERCISE 2: Resize and reduce image quality using FFmpeg

def resize_and_reduce_quality(input_image, output_image, width, height, quality):
    # Define an FFmpeg command to resize and reduce image quality
    ffmpeg_command = ['ffmpeg', '-i', 
    input_image, 
    '-vf', 
    f'scale={width}:{height}', 
    '-q:v', str(quality), 
    output_image
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)  # Run the FFmpeg command
        print(f"Image resized and quality reduced: {input_image} -> {output_image}")
    except subprocess.CalledProcessError:
        print("Error: FFmpeg command failed")

# EXERCISE 3: Serpentine byte rearrangement

def serpentine(input_file, output_file, step_size):
    with open(input_file, 'rb') as input_image:
        with open(output_file, 'wb') as output_image:
            byte = input_image.read(1)
            is_skipping = False  # Flag to determine if we should skip or read the byte
            while byte:
                output_image.write(byte)
                if is_skipping:
                    input_image.seek(step_size - 1, 1)  # Skip bytes based on the step_size
                is_skipping = not is_skipping
                byte = input_image.read(1)

# EXERCISE 4: Convert to black and white with compression using FFmpeg

def convert_to_bw_and_compress(input_file, output_file, quality=0):
    # Define an FFmpeg command to convert to black and white with compression
    ffmpeg_command = ['ffmpeg', '-i', input_file,
        '-vf', 'format=gray',  # Convert to grayscale
        '-qscale:v', str(quality),  # Use qscale:v to control the video quality
        output_file
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)  # Run the FFmpeg command
        print(f"Image transformed to black and white with high compression: {output_file}")
    except subprocess.CalledProcessError:
        print("Error: FFmpeg command failed")

# EXERCISE 5: Run-length encoding of a series of bytes

def run_length_encode(data):
    if not data:
        return b""  # Return an empty byte string if the input is empty

    encoded_data = bytearray()
    current_byte = data[0]
    count = 1

    for byte in data[1:]:
        if byte == current_byte:
            count += 1
        else:
            encoded_data.append(count)  # Append the count
            encoded_data.append(current_byte)  # Append the repeated byte
            current_byte = byte  # Update the current byte
            count = 1

    encoded_data.append(count)  # Append the final count
    encoded_data.append(current_byte)  # Append the final byte

    return bytes(encoded_data)

# EXERCISE 6: DCTTransform class for DCT encoding and decoding

class DCTTransform:
    def __init__(self):
        pass

    @staticmethod
    def forward_dct(data):
        """
        Perform forward DCT (encoding) on the input data.
        :param data: Input data (2D NumPy array)
        :return: DCT coefficients
        """
        return numpy.fft.dct(numpy.fft.dct(data, axis=0, norm='ortho'), axis=1, norm='ortho')

    def inverse_dct(dct_coeffs):
        """
        Perform inverse DCT (decoding) to recover the original data.
        :param dct_coeffs: DCT coefficients (2D NumPy array)
        :return: Decoded data
        """
        return numpy.fft.idct(numpy.fft.idct(dct_coeffs, axis=0, norm='ortho'), axis=1, norm='ortho')

def main():
    while True:
        print("Choose an option")
        print("1. RGB to YUV conversion")
        print("2. YUV to RGB conversion.")
        print("3. Resize and reduce the quality of an image")
        print("4. Serpentine rearrangement of bytes in an image")
        print("5. Convert an image to B&W with compression")
        print("6. Run-length encoding of a series of bytes")
        print("7. Quit")
        
        choice = input("Enter your choice:")

        if choice == "1":
            R = float(input("R (0 to 255): "))
            G = float(input("G (0 to 255): "))
            B = float(input("B (0 to 255): "))
            Y, U, V = rgb_to_yuv(R, G, B)
            print(Y, U, V)

        elif choice == "2":
            Y = float(input("Y (0 to 255): "))
            U = float(input("U (-128 to 127): "))
            V = float(input("V (-128 to 127): "))
            R, G, B = yuv_to_rgb(Y, U, V)
            print(R, G, B)

        elif choice == "3":
            input_image = input("Input Image File: ")
            output_image = input("Output Image File: ")
            width = int(input("Width (pixels): "))
            height = int(input("Height (pixels): "))
            quality = int(input("Quality (0-31): "))
            resize_and_reduce_quality(input_image, output_image, width, height, quality)
        
        elif choice == "4":
            input_file = input("Input File: ")
            output_file = input("Output File: ")
            step_size = 2  # Adjust the step size as needed
            serpentine(input_file, output_file, step_size)

        elif choice == "5":
            input_file = input("Input File: ")
            output_file = input("Output File: ")
            quality = 10  # Adjust the quality value as needed

            convert_to_bw_and_compress(input_file, output_file, quality)

        elif choice == "6":
            data = b'\x01\x01\x01\x02\x02\x03\x03\x03\x03'
            encoded_data = run_length_encode(data)
            print(encoded_data)
        
        elif choice == "7":
            print("Goodbye")
            break        
        
        else:
            print("Choose a correct option")

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
