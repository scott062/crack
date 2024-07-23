# String Compression


def string_compression(text):
    compressed_string = [] 
    ref_char = ""
    count = 0
    for char in text:
        if char == ref_char:
            count += 1
        else:
            if count and ref_char:
                compressed_string.append(f"{count}{ref_char}")
            ref_char = char
            count = 1
    compressed_string.append(f"{count}{ref_char}")
    return min("".join(compressed_string), text, key=len)

print(string_compression("a")) # => a
print(string_compression("aaaaaaaa")) # => 8a
print(string_compression("abcdefghijk")) # => abcdefghijk 
print(string_compression("aaaaaaaaaabcdefggggggggggggggggggg")) # => 10a1b1c1d1e1f419g

        
