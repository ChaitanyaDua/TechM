import csv

import openai
import streamlit as st

openai.api_key='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'
csv_file_path='/Users/chaitanyadua/Desktop/Health Portal/output.csv'
def main():
    with open(csv_file_path,'w',newline='') as file:
        writer=csv.writer(file)
        # Write the header row
        writer.writerow(['query', 'answer'])
        mylist=[]
        # file_path = 'bard_input.txt'  # Replace with the actual file path
        # Upload the text file
        txt_file = st.file_uploader("Upload your text file", type="txt")

        # Read the text file character by character
        if txt_file is not None:
        # Open the text file in read mode
            with txt_file as file:
            # Read the content of the file
                content = file.read().decode('utf-8')
            # Iterate through each character in the content
                # for char in content:
                # Process each character as needed
                    # print(char)

        # file_path = 'path/to/your/file.txt'  # Replace with the actual file path
                flag=0
                query="i want the root cause to be summarized for asset: orders, in maximum 100 words from "
                for char in content:

        # try:
        #     with open(file_path, 'r') as file:
        #         while True:
        #             char = file.read(1)
                    # if not char:
                        # break
                    query+=char
                mylist.append(query)
                    # if char=='{':
                    #     query+=char
                    #     flag=1
                    #     continue
                    # elif flag==1:
                    #     if char=='{' and content[i+2]=='D':
                    #         query="i want the root cause to be summarized for asset: orders, in maximum 25 words from "
                    #         query+=char
                    #     elif char=='}':
                    #         query+=char
                    #         mylist.append(query)
                    #     else:
                    #         query+=char
                # for i in range(5):
                    # print(mylist[i])
        # except FileNotFoundError:
        #     print("File not found.")
        # except IOError:
        #     print("Error reading the file.")
        # except IOError:
        #     print("Error reading the file.")
        st.title("Welcome!.Root Cause for DB errors")
        for item in mylist:
            user_input=item
        #     if st.button("Get Answer"):
            respose=openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7
        )
            answer=respose.choices[0].text.strip()
            # print(answer)
            # st.write("Answer: ",answer)
            writer.writerow([user_input, answer])
        # newquery=""
        # for item in mylist:
        #     newquery+=item
        # user_input=newquery
        # respose=openai.Completion.create(
        # engine="text-davinci-003",
        # prompt=user_input,
        # max_tokens=1000,
        # n=1,
        # stop=None,
        # temperature=0.7
        # )
        # answer=respose.choices[0].text.strip()
        # print(answer)

if __name__ == "__main__":
    main()

 
