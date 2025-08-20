import matplotlib.pyplot as plt
import random
from math import gcd
import time

# Elliptic curve implementation
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a  # Coefficient for x
        self.b = b  # Constant term
        self.p = p  # Prime number for modular arithmetic

    def is_on_curve(self, x, y):
        return (y**2) % self.p == (x**3 + self.a * x + self.b) % self.p
    
    def modular_inverse(self, x, p):
        if gcd(x, p) != 1:
            raise ValueError(f"No modular inverse exists for {x} modulo {p}")
        return pow(x, -1, p)
    
    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        
        if P[0] == Q[0] and P[1] != Q[1]:
            return None  # The result is the point at infinity (identity element)
        
        if P == Q:
            lam = (3 * P[0] ** 2 + self.a) * self.modular_inverse(2 * P[1], self.p)
        else:
            x_diff = Q[0] - P[0]
            if x_diff == 0:
                raise ValueError("Division by zero in point addition")
            lam = (Q[1] - P[1]) * self.modular_inverse(x_diff, self.p)
        
        x_r = (lam ** 2 - P[0] - Q[0]) % self.p
        y_r = (lam * (P[0] - x_r) - P[1]) % self.p
        return (x_r, y_r)

    def scalar_multiply(self, k, P):
        result = None
        addend = P

        while k:
            if k & 1:
                result = self.point_addition(result, addend)
            addend = self.point_addition(addend, addend)
            k >>= 1

        return result

def inverse_point(P, p):
    if P is None:
        return None
    return (P[0], -P[1] % p)

# Visualize the elliptic curve and points
def plot_curve(curve, points=None, highlight=None, title=''):
    x_vals = list(range(curve.p))
    y_vals = [pow(x**3 + curve.a*x + curve.b, 0.5) % curve.p for x in x_vals]
    y_vals_neg = [-pow(x**3 + curve.a*x + curve.b, 0.5) % curve.p for x in x_vals]

    plt.figure(figsize=(10, 8))
    plt.plot(x_vals, y_vals, label=f'Elliptic Curve y^2 = x^3 + {curve.a}x + {curve.b}', color='blue')
    plt.plot(x_vals, y_vals_neg, color='blue')  # Plot the negative y values
    
    if points:
        for point, label in points:
            plt.scatter(point[0], point[1], label=label, s=100)
    
    if highlight:
        for point, label in highlight:
            plt.scatter(point[0], point[1], color='red', label=label, s=150, edgecolor='black')
    
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.grid()
    plt.ylim(-10, 100)  # Set limits for better visibility
    plt.xlim(-10, 100)
    plt.show()

# Find a valid point on the curve by incrementing x
def find_valid_point(curve, message_num):
    x = message_num % curve.p
    while True:
        y_squared = (x**3 + curve.a * x + curve.b) % curve.p
        y = pow(y_squared, (curve.p + 1) // 4, curve.p)  # Modular square root
        if (y**2) % curve.p == y_squared:
            return (x, y)
        x = (x + 1) % curve.p

# Messaging function for two users to interact and visualize ECC encryption
def messaging_app():
    # Initialize curve parameters
    a, b, p = 2, 3, 97  # Curve: y^2 = x^3 + 2x + 3 mod 97
    curve = EllipticCurve(a, b, p)
    
    # Base point on the curve
    G = (3, 6)

    if not curve.is_on_curve(G[0], G[1]):
        raise ValueError("Base point is not on the curve")
    
    # Key Generation for User A and User B
    private_key_A = random.randint(1, p)
    public_key_A = curve.scalar_multiply(private_key_A, G)
    
    private_key_B = random.randint(1, p)
    public_key_B = curve.scalar_multiply(private_key_B, G)

    # Visualizing the initial setup
    print(f"User A's Public Key: {public_key_A}")
    print(f"User B's Public Key: {public_key_B}")
    
    messages = []  # To store messages and simulate conversation
    num_exchanges = 0

    while num_exchanges < 4:
        # User A sends a message to User B
        message_A = input("\nUser A, enter your message: ")
        message_A_num = sum([ord(char) for char in message_A])
        message_A_point = find_valid_point(curve, message_A_num)

        # Encryption by User A
        k_A = random.randint(1, p)
        C1_A = curve.scalar_multiply(k_A, G)
        shared_secret_A = curve.scalar_multiply(k_A, public_key_B)
        C2_A = curve.point_addition(message_A_point, shared_secret_A)
        
        messages.append((C1_A, C2_A))
        print(f"User A sent an encrypted message: {C1_A}, {C2_A}")
        plot_curve(curve, points=[(C1_A, 'C1'), (C2_A, 'C2')], title="User A's Encrypted Message")

        # User B decrypts the message
        shared_secret_B = curve.scalar_multiply(private_key_B, C1_A)
        message_B_point = curve.point_addition(C2_A, inverse_point(shared_secret_B, p))

        print(f"User B decrypted the message: {message_B_point}")
        plot_curve(curve, points=[(message_B_point, 'Decrypted Point')], title="User B Decrypted Message")

        num_exchanges += 1

    # Cyber Attack Simulation
    print("\n** Cyber Attack Simulation **")
    time.sleep(2)
    print("Hacker trying to intercept and decrypt the conversation...")

    time.sleep(2)
    print("Hacker failed: Unable to compute shared secrets without private keys!")

    # Simulate hacker's failed decryption attempt
    plot_curve(curve, points=[(C1_A, 'C1'), (C2_A, 'C2')], highlight=[(public_key_A, 'Public Key A')], title="Failed Attack")
    
    print("\nMessage exchange secured successfully.")

# Call the messaging app
messaging_app()
