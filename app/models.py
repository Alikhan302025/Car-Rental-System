from dataclasses import dataclass
from datetime import date


@dataclass
class Vehicle:
    vehicle_id: int
    brand: str
    model: str
    year: int

    def get_info(self) -> str:
        return f"{self.brand} {self.model} ({self.year})"


@dataclass
class Car(Vehicle):
    daily_price: int
    branch_id: int

    def calculate_price(self, days: int) -> int:
        return self.daily_price * days


@dataclass
class Customer:
    customer_id: int
    first_name: str
    last_name: str
    telegram_id: int

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


@dataclass
class Rental:
    rental_id: int
    customer_id: int
    car_id: int
    start_date: date
    end_date: date
    status: str

    def rental_days(self) -> int:
        return (self.end_date - self.start_date).days


@dataclass
class DamageReport:
    report_id: int
    rental_id: int
    description: str
    repair_cost: int
