from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import uvicorn
app = FastAPI()

class InputData(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def bfhl(input_data: InputData):
    arr = input_data.data
    
    evens, odds, alphabets, specials = [], [], [], []
    total_sum = 0

    for item in arr:
        if item.isdigit():  
            num = int(item)
            total_sum += num
            if num % 2 == 0:
                evens.append(item)  
            else:
                odds.append(item)
        elif item.isalpha():  
            alphabets.append(item.upper())
        else:  
            specials.append(item)
    
    concat_alpha = "".join(alphabets[::-1])
    alternating_caps = "".join(
        ch.lower() if i % 2 else ch.upper()
        for i, ch in enumerate(concat_alpha)
    )

    return {
        "is_success": True,
        "user_id": "john_doe_17091999",   
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odds,
        "even_numbers": evens,
        "alphabets": alphabets,
        "special_characters": specials,
        "sum": str(total_sum),
        "concat_string": alternating_caps
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

