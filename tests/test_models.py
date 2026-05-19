from datetime import date

from app.models import Car, Customer, Rental


def test_car_get_info():
    car = Car(
        vehicle_id=1,
        brand="Toyota",
        model="Camry",
        year=2020,
        daily_price=15000,
        branch_id=1
    )

    assert car.get_info() == "Toyota Camry (2020)"


def test_car_calculate_price():
    car = Car(
        vehicle_id=1,
        brand="Toyota",
        model="Camry",
        year=2020,
        daily_price=15000,
        branch_id=1
    )

    assert car.calculate_price(3) == 45000


def test_customer_full_name():
    customer = Customer(
        customer_id=1,
        first_name="Alikhan",
        last_name="Zhambayev",
        telegram_id=123456
    )

    assert customer.full_name() == "Alikhan Zhambayev"


def test_rental_days():
    rental = Rental(
        rental_id=1,
        customer_id=1,
        car_id=1,
        start_date=date(2026, 5, 1),
        end_date=date(2026, 5, 5),
        status="active"
    )

    assert rental.rental_days() == 4