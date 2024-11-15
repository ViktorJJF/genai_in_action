import getpass
import os

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
    
    
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.2-90b-text-preview",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

context="""En Mifarma los descuentos sí se sienten
Descuentos exclusivos en Mifarma.com.pe
Ya sea que busques productos de Cuidado Personal, como tratamientos capilares, pañales ecológicos para bebés, entre otros, en Mifarma Online tenemos todo lo que necesitas y mucho más. Mifarma Perú se diferencia de los demás ecommerce por sus atractivos descuentos y el programa de fidelización preferido por muchos: El monedero del ahorro Digital. Afíliate en nuestras boticas, app o web para sumar puntos, tener cupones personalizados y cientos de descuentos adicionales.

En Boticas Mifarma nos esforzamos por brindarte las mejores ofertas y descuentos para que puedas cuidar de ti y de tus seres queridos sin comprometer tu bolsillo. Pero no solo se trata de los descuentos, si buscas orientación farmacéutica, llama al (01)612-5000 que uno de nuestros técnicos farmacéuticos te atenderá las 24 horas, los 365 días del año. Además, con nuestro servicio Botica delivery, recibirás tus productos directamente en la puerta de tu hogar y tenemos despacho 24 horas en los distritos de Surquillo, San Borja, Miraflores y San Isidro. En Mifarma tu bienestar es primero y ahorra con el cuponero Mifarma.

Cyber Wow en Mifarma
Aprovecha las mejores ofertas que trae el Cyber Wow en Mifarma. Solo durante cinco días, consigue descuentos únicos en cosméticos, cremas hidratantes, cuidado infantil, dermocosmética, cuidado personal, adulto mayor, tratamientos capilares y mucho más. ¡Ahorros que Hacen Bien! Aumenta tus ofertas este Cyber Wow pagando con Agora y Oh! Pay.

Cyber Mifarma
Los mejores días para comprar online llegaron con descuentos en tus marcas favoritas, cremas corporales, nutrición infantil, vitaminas, colágenos, productos de belleza y cuidado personal. Regístrate y sé el primero en disfrutar de todos los beneficios que tenemos para ti durante el Cyber Day Mifarma.

Vital Vitaminado en Mifarma
Vital Vitaminado es una marca de suplementos que contienen nutrientes, vitaminas y minerales que favorecen una nutrición balanceada, apoyando el bienestar general y una vida saludable: Vital vitaminado Gluco control Sabor vainilla es una mezcla de alimentos libre de azúcar y que puede ser consumido como parte de una alimentación saludable. Es ideal para personas diabéticas y para quienes quieran controlar su consumo de azúcar. Vital Vitaminado Beauty Sabor vainilla es un multivitamínico a base de colágeno, coenzima Q10, proteínas y fibra que contribuyen a que la mujer se sienta activa y saludable. Vital Vitaminado Crecimiento Pediátrico cuenta con nutrientes esenciales que favorecen el crecimiento como proteínas, calcio, zinc DHA, ARA, Omega 3, Pre y Probióticos que apoyan el desarrollo integral de niños mayores de 2 años hasta la adolescencia.

Encuentra asesoría de salud en Aló Mifarma
¡En boticas Mifarma nos preocupamos por tu bienestar! Encuentra la orientación farmacéutica que necesitas llamando al (01)612-5000 opción 3 y comunícate con nuestro personal calificado las 24 horas, los 365 días del año, a través de nuestro servicio de farmacia delivery, quienes te brindarán tanto seguridad como confianza en tus consultas, y pedidos.

Además de la atención personalizada, disfruta del servicio de Mifarma Delivery, recibe tus pedidos en la puerta de tu casa y elige el método de pago contra entrega que mejor se te acomode: en efectivo o con tarjeta de crédito | débito.

*Contamos con despacho 24 horas para los distritos de Surquillo, San Borja, Miraflores y San Isidro.
¿Cuál es la ventaja de comprar en Mifarma online?
Comprar en Mifarma tiene varias ventajas. En primer lugar, disfruta de la comodidad de comprar desde casa y recibir los productos directamente en tu puerta. Además, contamos con promociones y descuentos exclusivo online en muchos productos. Programa tu entrega de acuerdo a tu disponibilidad y paga con efectivo, tarjeta de crédito o débito desde la misma web o al recibir tus productos. En Mifarma delivery la diferencia está en los descuentos

¿Cómo puedo realizar una compra en Mifarma Online?
Para realizar una compra en Mifarma Online, visita nuestra página web o app, busca los productos que deseas adquirir con descuentos especiales, agrégalos al carrito de compra y sigue los pasos indicados para finalizar el pedido.

¿Cuáles son los métodos de pago aceptados en Mifarma Online?
En Mifarma aceptamos diversos métodos de pago, como tarjetas de crédito y débito (Visa, MasterCard) y efectivo. Si pagas con Oh! Pay y Agora, recibe descuentos adicionales en tus compras.

¿Cuánto tiempo tarda en llegar mi pedido?
El tiempo de entrega de tu pedido dependerá de tu ubicación y del método de envío seleccionado. Mifarma Online se esfuerza por realizar envíos rápidos y eficientes para que recibas tus productos en el menor tiempo posible.

Blog Mifarma
¿Buscas información sobre belleza, salud y bienestar? Descubre nuestro blog en Mifarma. Te ofrecemos contenido valioso y actualizado sobre cuidado personal, tendencias en cosmética y estilo de vida saludable.

Categorías y marcas top en Mifarma
En Mifarma los descuentos sí se sienten. Por eso, es una de las tiendas online preferidas por quienes buscan promociones y descuentos en Farmacia, pañales, Belleza, Nutrición, Cuidado Personal, entre otros, por su amplia gama de productos, que incluyen productos de farmacia, suplementos nutricionales, condones, pañales ecológicos de las marcas top y más.

Mifarma es Dermocosmética
Tenemos descuentos en productos para el cuidado de la piel infantil, cuidado de la cara, cuidado del cabello, fotoprotección y mucho más. Además, encuentra ofertas en faciales, lociones limpiadoras y micelares de las marcas Avéne, Vichy, Eucerin, La Roche Posay y Bioderma. Si quieres saber más sobre cómo cuidar tu piel, te invitamos a visitar nuestro blog en Mundo Dermo.

Mifarma es Cuidado Personal
Luce un nuevo peinado, disfruta de un masaje relajante, cuida tu piel y mucho más en nuestra departamento de Cuidado Personal donde encontrarás productos para el Cuidado del cabello, Cuidado bucal, Desodorantes, Jabones, preservativos todo para un Afeitado espectacular.

Mifarma es Belleza
Embellece tu cutis, mejora el contorno corporal y cuida tu cabello eligiendo el producto ideal en nuestra categoría Belleza en Mifarma y ahorra en productos como Bloqueadores solares, Accesorios de belleza, Cuidado facial, Tintes para cabello, Cosméticos y marcas top como Cerave, Neutrogena y Nivea.

Los Packs del Ahorro en Mifarma
En Mifarma.com.pe queremos verte siempre bien. Por esta razón, te presentamos nuestro departamento de Packs del Ahorro con mayores descuentos en tus productos y marcas de tu preferencia como pañales, vitaminas, cuidado capilar y mucho más. Si compras en Pack, ahorras más. Estas son nuestras categorías del ahorro: Ahorra en Nutrición Infantil, Ahorra en Belleza, Ahorra en Cuidado Infantil, Ahorra en Nutrición y Bienestar, Ahorra en Cuidado Personal, Ahorra en Cuidado del Adulto Mayor, Ahorra en Dermocosmética y Ahorra en Farmacia.

Aliviamed
¡Salud de calidad con Aliviamed: Consultas médicas a tu alcance pagando S/.19! Un médico te atenderá telefónicamente y te brindará el diagnóstico y tratamiento de acuerdo a los síntomas que describas. ¡Fácil, rápido y a tu alcance! Adquiere tu consulta en nuestras boticas Mifarma o llamando a Aló Mifarma (01) 612-5000.

¡Tu Monedero del Ahorro ahora también es digital!
El Monedero del Ahorro es el programa de fidelización de Mifarma que ahora también es digital. Afíliate al Monedero del Ahorro Mifarma en nuestras boticas, web o app para sumar puntos, tener cupones personalizados y cientos de descuentos.

Beneficios exclusivos para socios del Monedero del Ahorro
Acumula Puntos-Dinero: Puedes usar tus puntos dinero para pagar parte o el total de tu compra. 

Cupones de descuento. Tienes descuentos adicionales y con tu Monedero del Ahorro Digital tienes cupones personalizados.

Compras con descuentos. En muchas de tus compras puedes obtener descuentos, que reducen el monto que tienes que pagar. ¡El ahorro es inmediato!

¿Cómo acumulo Puntos Dinero con el Monedero del Ahorro Mifarma Perú? 
Si estás afiliado al Monedero del Ahorro Digital acumularás 01 punto-dinero por cada S/1.00 de consumo en boticas, web o app. Y si usas solo el Monedero del Ahorro Tradicional acumularás 01 punto-dinero por cada S/2.00 de consumo en boticas, web o app.

Por cada cien (100) Puntos - Dinero acumulados obtendrás S/1.00 de descuento.

Entérate de los términos y condiciones del programa aquí.

Botica Delivery
Mifarma se posiciona como una destacada botica que sobresale por su eficiente servicio de farmacia delivery. Con un enfoque en la comodidad y accesibilidad, Mifarma ofrece a sus clientes la conveniencia de recibir productos a domicilio. Este servicio de botica delivery garantiza que los clientes puedan acceder de manera rápida y segura a una amplia gama de productos, convirtiendo a Mifarma en una opción confiable para satisfacer las necesidades de salud y bienestar.

Los Días Oh! con Cyber Ofertas
Prepárate para los Días Oh! en Mifarma, el evento de Cyber Ofertas más esperado del año en productos de dermocosmética, cuidado personal, bienestar y mucho más. Del 21 al 25 de octubre, sumérgete en un mundo de descuentos irresistibles en Mifarma online. Durante estos Días Oh!, encontrarás ofertas exclusivas en tus marcas de belleza preferidas para renovar tu rutina de cuidado o adelantar tus compras navideñas. No pierdas la oportunidad de aprovechar estas Cyber Ofertas únicas y dale a tu piel, cabello y bienestar general el mimo que se merecen. ¡Marca en tu calendario los Días Oh! de Mifarma y prepárate para una experiencia de compra online extraordinaria!"""

messages = [
    (
        "system",
        f"You are a helpful assistant who speaks spanish. You only know the provided context inside ```...```\nContext\n```{context}```",
    )
]

while True:
    input_message=input("Tu mensaje: ")
    messages.append(("human", input_message))
    ai_msg = llm.invoke(messages)
    ai_content=ai_msg.content
    print("AI: ",ai_content)
    print("Usage: ",ai_msg.response_metadata.get("token_usage"))
    messages.append(("assistant", ai_content))
    

    

