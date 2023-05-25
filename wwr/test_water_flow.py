from pytest import approx
import pytest

def water_column_height(tower_height, tank_height):
    water = tower_height + (3 * tank_height) / 4
    return water

def test_water_column_height():
    assert water_column_height(0, 0) == approx(0)
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == approx(25)
    assert water_column_height(48.3, 12.8) == approx(57.9)

def pressure_gain_from_water_height (height):
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0)
    assert pressure_gain_from_water_height(30.2) == approx(295.628)
    assert pressure_gain_from_water_height(50) == approx(489.450)

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
       pressure_loss = (-friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2000 * pipe_diameter)
       return pressure_loss

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
