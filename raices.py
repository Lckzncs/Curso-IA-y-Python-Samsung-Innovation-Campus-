import math


def resuelve_ecuacion(a, b, c):
    """
    Resuelve una ecuacion de segundo grado a x^2 + bx + c = 0.

    Parameters
    ----------
    a : float
        Coeficiente de segundo grado. No puede ser cero.
    b : float
        Coeficiente de primer grado.
    c : float
        Término independiente.

    Returns
    -------
    Una tupla con las raíces reales.

    Throws
    ------
    ValueError si no hay dos soluciones reales.
    """

    if a == 0:
        raise ValueError("la ecuación no es de segundo grado")
    else:
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            raise ValueError("las raíces son complejas")
        else:
            raiz_discriminante = math.sqrt(discriminante)
            raices = ((-b + raiz_discriminante) / (2 * a),
                      (-b - raiz_discriminante) / (2 * a))
            return raices