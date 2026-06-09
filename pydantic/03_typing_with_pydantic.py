from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    id: int
    user_id: int
    items: List[str] # List with string value
    quantities:  Dict[str, int] # Dictionary with string key and integer value
    total_price: float = 0.0
    currency: Optional[str] = 'INR' # It can be str or it can be 'INR'
    

cart = Cart(
    id=1,
    user_id=1,
    items=['Mouse', 'Keyboard'],
    quantities={
        'Mouse': 10,
        'Keyboard': 12
    }
)

print(cart)