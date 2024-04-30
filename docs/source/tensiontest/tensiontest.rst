Tension test
============

.. toctree::
   :maxdepth: 2

   specimens

important Attributes for a tension test [ISO 6892-1:2016(E)]

* ao [mm] ... original thickness of a flat test piece or wall thickness of a tube
* bo [mm] ... original width of the parallel length of a flat test piece or average width of the longitudinal strip taken from a tube or width of flat wire
* do [mm] ... original diameter of the parallel length of a circular test piece, or diameter of round wire or internal diameter of a tube
* Do [mm] ... original external diameter of a tube
* Lo [mm] ... original gauge length
* So [mm²] ... original cross-sectional area of the parallel length
* Su [mm²] ... minimum cross-sectional area after fracture
* A [%] ... percentage elongation after fracture
* Ag [%] ... percentage plastic extension at maximum force, Fm
* Agt [%] ... percentage total extension at maximum force, Fm
* At [%] ... percentage total extension at fracture
* dLm [mm] ... extension at maximum force
* dLf [mm] ... extension at fracture
* Fm [N] ... maximum force
* e.Le [1/s] ... strain rate

References
----------

* TechReport (DIN6892-1) ISO 6892-1:2009, Metallische Werkstoffe – Zugversuch – Teil 1: Prüfverfahren bei Raumtemperatur 2009
* TechReport (DIN6892-2) ISO 6892-2:2009, Metallische Werkstoffe – Zugversuch – Teil 2: Prüfverfahren bei erhöhter Temperatur 2009
* ISO 6892-1:2016(E)
* VDA 238-100 2010:12
* Weißbach, W. Werkstoffkunde und Werkstoffprüfung: Strukturen, Eigenschaften, Prüfung Vieweg, 2007

Brucheinschnürung

.. math::

    Z = \frac{S_o-S_u}{So}

Bruchdehnung

.. math::

    A = \frac{L_u-L_o}{L_o}

Zugfestigkeit

.. math::

    R_m = \frac{F_m}{S_o}


Einschnürung [Semiatin1985, Gerhardt2015]

a: Probenbreite in der Einschnürung
R: Krümmungsradius in der Einschnürung


.. math::

    k_{f}=\frac{F}{A_{\min }} \cdot \frac{1}{\sqrt{1+\frac{R}{a}} \cdot \ln \left(1+\frac{a}{2 R}+\sqrt{\frac{a}{R} \cdot\left(1+\frac{a}{4 R}\right)}-1\right)}