key_map = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
    18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}


def getDecodedMessages(message,index):
    if(index==len(message)):
        return [""]
    elif index>len(message):
        return []
    elif message[index]=="0":
        return []
    decoded_messages = []
    current_num = int(message[index])
    decoded_messages_using_current_num = getDecodedMessages(message,index+1)
    for decoded_message in decoded_messages_using_current_num:
        decoded_messages.append(key_map[current_num] + decoded_message)
    if index+1<len(message):
        extended_num = int(message[index]+message[index+1])
        if int(extended_num)<=26:
            decoded_messages_using_extended_num = getDecodedMessages(message,index+2)
            for decoded_message in decoded_messages_using_extended_num:
                decoded_messages.append(key_map[extended_num] + decoded_message)
    return decoded_messages


message = input("please neter a message")
print(getDecodedMessages(message,0))


#link to similar question -> https://leetcode.com/problems/decode-ways/description/