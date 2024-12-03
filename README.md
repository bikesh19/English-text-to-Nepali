
# Roman to Nepali Script Converter 🗣️➡️📝

This is a Python script for converting Romanized Nepali text into Nepali script. It uses a dictionary-based mapping approach to transliterate characters and supports vowels, consonants, numbers, and special characters.

## Features ✨

- 🔠 Converts Romanized Nepali to Nepali script (e.g., `kaam garna` → `काम गरन`).
- 🛠️ Handles multi-character combinations intelligently (e.g., `kri` → `कृ`).
- 📜 Supports Nepali numbers, punctuation, and conjuncts.
- 🌐 Perfect for creating Nepali content from Romanized text.

## How It Works 🔍

1. **Dictionary Mapping**: 
   - A dictionary (`romanized_english_to_nepali_dict`) maps Roman characters to their Nepali equivalents.
   
2. **Text Processing**: 
   - The script checks for the longest possible match in the input text using the `broken_text` function.
   - Matches are appended sequentially to form the final Nepali text.

3. **Real-Time Conversion**:
   - Users provide Romanized Nepali text through input.
   - The converted Nepali script is displayed as output.

## Usage 🛠️

1. **Clone the Repository**:
   git clone https://github.com/bikesh19/Romanized_English-text-to-Nepali
   cd roman-to-nepali-converter

2. **Run the Script**:
      python roman_to_nepali.py
   
3. **Input Romanized Nepali**:
   Enter text like `kaam garna` when prompted.

4. **See the Output**:
   The script will print the converted Nepali text, e.g., `काम गरन`.

## Example 🚀

Input:  
enter text in nepali: kaam garna jaaun

Output:  
काम गरन जाउन

## File Structure 📂

romanized_english_to_nepali_converter<br>
│<br>
├── main.py   <br>
├── dict.txt <br>
└── README.md  <br>

## Future Enhancements 🚀

- Add support for more dialects and regional nuances.
- Develop a GUI version for non-technical users 🖥️.
- Integrate with popular text editors and IDEs for seamless Nepali typing.

## License 📝

This project is open-source under the MIT License.
