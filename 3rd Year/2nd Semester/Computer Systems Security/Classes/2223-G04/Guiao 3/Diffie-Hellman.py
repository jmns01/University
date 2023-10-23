import random
from cryptography.hazmat.primitives.asymmetric import dh


P = 99494096650139337106186933977618513974146274831566768179581759037259788798151499814653951492724365471316253651463342255785311748602922458795201382445323499931625451272600173180136123245441204133515800495917242011863558721723303661523372572477211620144038809673692512025566673746993593384600667047373692203583
G = 44157404837960328768872680677686802650999163226766694797650810379076416463147265401084491113667624054557335394761604876882446924929840681990106974314935015501571333024773172440352475358750668213444607353872754650805031912866692119819377041901642732455911509867728218394542745330014071040326856846990119719675

def keyGenereator():
    key = random.randint(1,10^1000)
    return key


def alice():
    privateKey = keyGenereator()

    A = G^privateKey % P
    return A, privateKey



def bob():
    privateKey = keyGenereator()

    B = G^privateKey % P
    return B, privateKey


def main():
    A, pkA = alice()
    B, pkB = bob()

    kAlice = B ^ pkA % P
    kBob = A ^ pkB % P

    print(kAlice)
    print(kBob)
    print(kBob == kAlice)

main()
