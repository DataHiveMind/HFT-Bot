import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass
class Basic_HFT():
    order_quantity: int
    market_depth: int

def calculate_price():
    raise NotImplementedError

def simulate_order():
    raise NotImplementedError
