from uuid import uuid4
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from embeding import vector_store  # Replace 'my_project' with the actual module path
from langchain_core.documents import Document

document_1 = Document(
    page_content="For a typical plot size of 25 feet by 50 feet, a suggested layout includes 2 bedrooms—one master bedroom measuring 12 by 14 feet and a secondary bedroom measuring 10 by 12 feet. A drawing room of 10 by 12 feet and a spacious living room or TV lounge of 12 by 15 feet are recommended. The kitchen, either open or semi-open, should be approximately 8 by 10 feet. The plan includes 2 attached bathrooms and a car porch suitable for one car. A small lawn or garden can be optionally placed at the front. If a double story is planned, the staircase should be located inside. The design should focus on efficient space utilization, particularly with an open kitchen-lounge combination.",
    metadata={"source": "5 marla double story house"},
)
document_2 = Document(
    page_content="For a 25 ft × 50 ft plot, this layout includes 2 bedrooms—a master bedroom measuring 11 by 14 feet and a secondary bedroom of 10 by 11 feet. The drawing room is 9 by 12 feet, and the TV lounge is 12 by 13 feet. The kitchen is open and measures 7 by 10 feet. There are 2 attached bathrooms, a car porch for one car, and a small front lawn. The staircase is located inside near the side wall, ideal for a potential double sory."  ,
    metadata={"source": "5 marla double story house"},
)
document_3 = Document(
    page_content="This layout is designed for a 25 ft × 50 ft plot, featuring a 13 by 12 feet master bedroom and a 10 by 10 feet secondary bedroom. The drawing room measures 10 by 11 feet, while the living area is 11 by 14 feet. The semi-open kitchen is 8 by 9 feet. The house includes 2 bathrooms, a 12 by 14 feet car porch, and a compact front garden. The staircase is centrally located for easy access if a second story is added  ",
    metadata={"source": "5 marla double story house"},
)
document_4 = Document(
    page_content="Built for a 25 ft × 45 ft plot, this design includes a master bedroom of 12 by 12 feet and a secondary bedroom of 10 by 12 feet. The drawing room and kitchen are both 10 by 10 feet and 6 by 9 feet respectively, with the kitchen designed in an open-plan format. The living area spans 13 by 14 feet. There are 2 attached bathrooms, a single-car porch, no lawn to maximize space, and an internal staircase near the kitchen.ion.",
    metadata={"source": "5 marla double story house"},
)
document_5 = Document(
    page_content="This 5 Marla plan features a 12 by 13 feet master bedroom and a 10 by 11 feet secondary bedroom. A 9 by 11 feet drawing room complements the spacious 12 by 15 feet TV lounge. The kitchen is 7 by 11 feet and opens into the lounge. Two attached bathrooms are included along with a covered car porch and a side garden strip. The staircase is external, located at the rear for separate access to the upper floor.",
    metadata={"source": "5 marla double story house"},
)
document_6 = Document(
    page_content="Ideal for a 25 ft × 50 ft plot, this house plan offers a 13 by 13 feet master bedroom and an 11 by 12 feet secondary bedroom. The drawing room measures 10 by 13 feet and the living room is 12 by 14 feet. The kitchen is 9 by 9 feet with an open island-style layout. It includes 2 attached bathrooms, a 12 by 15 feet car porch, a small front sitting lawn, and a compact indoor spiral staircase.",
    metadata={"source": "5 marla double story house"},
)
document_7 = Document(
    page_content="This layout features a 12 by 14 feet master bedroom and a 10 by 10 feet secondary bedroom on a 25 ft × 45 ft plot. A 10 by 12 feet drawing room and a 12 by 13 feet living room provide ample shared space. The kitchen, semi-open, is 8 by 10 feet. There are 2 bathrooms, a car porch for one sedan, minimal lawn space, and a staircase placed near the drawing room for potential upper-level expansion.",
    metadata={"source": "5 marla double story house"},
)
document_8 = Document(
    page_content="This single-story layout for a 25 ft × 50 ft plot includes a 12 by 14 feet master bedroom and a 10 by 11 feet secondary bedroom, both with attached bathrooms. The drawing room is 10 by 12 feet, and the lounge is 12 by 15 feet, combined with an 8 by 10 feet open kitchen. A car porch fits one car, with a small lawn in the front. Designed with wide corridors and ample natural light, this layout ensures comfort without needing a staircase.",
    metadata={"source": "5 marla single story house"},
)
document_9 = Document(
    page_content="Designed for compact functionality, this 5 Marla single-story house features two bedrooms: a 12 by 13 feet master bedroom and a 10 by 10 feet secondary bedroom. The living room is 12 by 14 feet, connected to an 8 by 9 feet semi-open kitchen. A 9 by 11 feet drawing room is located near the entrance. Two bathrooms are attached to the bedrooms. The car porch accommodates one vehicle, with a small garden space in front for a cozy look.",
    metadata={"source": "5 marla single story house"},
)
document_10 = Document(
    page_content="In this efficient single-floor layout, the house offers a 13 by 12 feet master bedroom and a 10 by 11 feet secondary bedroom, both with access to bathrooms. The 10 by 12 feet drawing room and the 12 by 13 feet lounge share space with a modern 8 by 8 feet open kitchen. A 12 by 14 feet car porch is provided, and a narrow side lawn brings in greenery. No stairs are included, keeping everything at ground level for easy access and aging-in-place design.",
    metadata={"source": "5 marla single story house"},
)
document_11 = Document(
    page_content="This modern 5 Marla single-story home includes a 12 by 12 feet master bedroom, a 10 by 12 feet secondary bedroom, and a 9 by 10 feet guest room. The kitchen is 8 by 9 feet in an open format, attached to a 12 by 14 feet living area. There are two bathrooms—one common and one attached. The car porch fits one car, and a small green patch in front adds visual appeal. This layout prioritizes flow and accessibility for ground-level living.",
    metadata={"source": "5 marla single story house"},
)
document_12 = Document(
    page_content="For a 30 ft × 60 ft plot (7 Marla, approx. 1575 sq. ft.), the layout includes 3 bedrooms—a 13 by 15 feet master bedroom and two 11 by 12 feet bedrooms—each with an attached bathroom. A 12 by 14 feet drawing room is formally separated from the 14 by 16 feet TV lounge. The kitchen is 10 by 12 feet. The house features a car porch that can fit one large or two small cars, a small front lawn, and a staircase that can be placed either inside or outside depending on whether a double unit is planned.",
    metadata={"source": "7 marla double story house"},
)
document_13 = Document(
    page_content="The ground floor includes a 13 × 15 ft master bedroom, a 12 × 14 ft drawing room, and a spacious 14 × 16 ft lounge connected to a 10 × 12 ft open kitchen. The first floor includes two 11 × 12 ft bedrooms with attached baths, a small sitting area, and a terrace. The internal staircase connects both floors for ease of access.",
    metadata={"source": "7 marla double story house"},
)
document_14 = Document(
    page_content="This layout provides a formal 12 × 14 ft drawing room and a 14 × 16 ft TV lounge on the ground floor, with a 13 × 15 ft master bedroom and 11 × 12 ft guest room. Upstairs features two more bedrooms, each 11 × 12 ft, a small lounge, and a balcony. The staircase is external, offering potential for independent upper-floor rental use.",
    metadata={"source": "7 marla double story house"},
)
document_15 = Document(
    page_content="The lower floor features a 13 × 15 ft master bedroom, an 11 × 12 ft guest room, and a 12 × 14 ft drawing room separated from the 14 × 16 ft lounge. A 10 × 12 ft open kitchen faces the lounge. The upper floor includes two bedrooms, a small study, and a kitchenette for partial independence. The staircase is internal.",
    metadata={"source": "7 marla double story house"},
)
document_16 = Document(
    page_content="On the ground floor, there’s a 13 × 15 ft master bedroom and 11 × 12 ft guest bedroom with attached baths, a 12 × 14 ft formal drawing room, and a 10 × 12 ft kitchen open to the 14 × 16 ft lounge. The first floor has a 13 × 14 ft bedroom, a home office, a laundry, and a large terrace. The staircase is inside.",
    metadata={"source": "7 marla double story house"},
)
document_17 = Document(
    page_content="Designed for families with guests or tenants, this plan offers a 2-bedroom lower floor with a formal drawing room and open kitchen-lounge design, while the upper floor includes two additional bedrooms, a separate lounge, and a balcony. External stairs allow independent access.",
    metadata={"source": "7 marla double story house"},
)
document_18 = Document(
    page_content="This open concept layout integrates the 10 × 12 ft kitchen with a 14 × 16 ft living room, and features a 13 × 15 ft master bedroom, an 11 × 12 ft kids' bedroom, and a multipurpose room. There’s a porch for one large car and a small garden space.",
    metadata={"source": "7 marla single story house"},
)
document_19 = Document(
    page_content="With emphasis on privacy and space, this plan includes a 13 × 15 ft master bedroom at the rear, two side-by-side 11 × 12 ft bedrooms, and a wide lounge-kitchen combo (14 × 18 ft total). The drawing room remains at the front for formal guests.",
    metadata={"source": "7 marla single story house"},
)
document_20 = Document(
    page_content="This plan features two bedrooms—13 × 15 ft and 11 × 12 ft—with a third flexible room used as a study or guest room. The 12 × 14 ft drawing room is placed next to a 14 × 16 ft lounge, and the open kitchen is 10 × 12 ft. The layout is ideal for nuclear families.",
    metadata={"source": "7 marla single story house"},
)
document_21= Document(
    page_content="The house includes a 13 × 15 ft master bedroom and two 11 × 12 ft bedrooms, each with attached baths. A 12 × 14 ft drawing room is placed at the front, separated from the 14 × 16 ft lounge, with a 10 × 12 ft semi-open kitchen. The front also features a car porch and a small lawn.",
    metadata={"source": "7 marla single story house"},
)
document_22 = Document(
    page_content="A 10 Marla house typically spans around 2250 square feet, with dimensions like 35 ft × 65 ft or 40 ft × 70 ft. The house includes 4 bedrooms—one on the ground floor for guests with an attached bathroom, and three on the upper floor, each with its own attached bath. A spacious 14 ft × 16 ft drawing room and a 12 ft × 14 ft dining room offer formal gathering spaces. The living or TV lounge measures 16 ft × 20 ft, connected to a 10 ft × 14 ft main kitchen and a 6 ft × 10 ft dirty kitchen. The house may also include 4 to 5 bathrooms, a servant room with a separate entrance (optional), a car porch for 2 vehicles, and medium-sized front and back lawns. Being a premium home, 10 Marla layouts often feature powder rooms, larger kitchens, and refined zoning between public and private spaces.",
    metadata={"source": "10 marla double story house"},
)
document_23 = Document(
    page_content="The ground floor includes a 14 × 16 ft drawing room and a 12 × 14 ft dining area, a spacious 16 × 20 ft lounge, a 10 × 14 ft main kitchen with an adjacent 6 × 10 ft dirty kitchen, and a 13 × 15 ft guest bedroom with an attached bath. The first floor offers three 12 × 14 ft bedrooms with attached baths, a small study, and a terrace. The servant room is accessible via a separate back staircase.",
    metadata={"source": "10 marla double story house"},
)
document_24 = Document(
    page_content="This layout features a front-facing drawing room and dining area, an open kitchen-lounge combo (with main and spice kitchens), and a guest suite on the ground floor. The upper floor includes a master bedroom with a walk-in closet, two other bedrooms with private bathrooms, and a cozy lounge space. The servant quarter is positioned over the garage for privacy.",
    metadata={"source": "10 marla double story house"},
)
document_25 = Document(
    page_content="The house is divided into formal and private zones. The ground floor includes a powder room near the entry, a 14 × 16 ft drawing room, a 16 × 20 ft living area, a main kitchen, and a guest bedroom. The upper floor offers three bedrooms, one with a private terrace, and a shared study or prayer room. A hidden staircase leads to the servant quarter, which is detached from the main house.",
    metadata={"source": "10 marla double story house"},
)
document_26= Document(
    page_content="A symmetrical layout places a guest bedroom with attached bath on one side and a drawing/dining area on the other, centered around a double-height 16 × 20 ft lounge. The first floor has a balcony, three bedrooms with dressing areas and attached baths, and a lounge overlooking the living area below. The design also includes a laundry and storage room upstairs.",
    metadata={"source": "10 marla double story house"},
)
document_27 = Document(
    page_content="This design includes a front-facing drawing room measuring 14 ft by 16 ft, a central lounge/TV room of 16 ft by 20 ft, and a spacious dining area of 12 ft by 14 ft. The kitchen layout features a 10 ft by 14 ft main kitchen along with a 6 ft by 10 ft dirty/spice kitchen. There are four bedrooms in total: a master bedroom sized 14 ft by 15 ft with a walk-in closet and an 8 ft by 6 ft attached bathroom, two secondary bedrooms each 12 ft by 14 ft with their own 7 ft by 6 ft attached baths, and a guest bedroom measuring 12 ft by 13 ft with an attached bath. A 6 ft by 5 ft powder room is also included. A car porch for two cars and a medium-sized lawn in the front and backyard complete the layout.",
    metadata={"source": "10 marla single story house"},
)
document_28 = Document(
    page_content="This layout emphasizes open spaces, starting with a 16 ft by 18 ft combined lounge and dining area. The drawing room is 14 ft by 16 ft, while the kitchen is an open-style 12 ft by 14 ft with an optional 6 ft by 8 ft spice kitchen. The master bedroom is 15 ft by 16 ft with a 9 ft by 6 ft attached bathroom. Two additional bedrooms are each 12 ft by 13 ft, and a fourth room can be used as a guest or study room, measuring 11 ft by 12 ft. Each bedroom includes attached baths. A powder room and a dedicated laundry area are included. A front and rear lawn provide outdoor relaxation space.",
    metadata={"source": "10 marla single story house"},
)
document_29 = Document(
    page_content="This premium single-story house includes a formal 14 ft by 16 ft drawing room, a 12 ft by 14 ft dining room, and a grand 18 ft by 20 ft lounge/TV room. The main kitchen is 10 ft by 14 ft with a 6 ft by 10 ft dirty kitchen. The master bedroom is 15 ft by 17 ft with an attached dressing area and bath. Two secondary bedrooms are 13 ft by 14 ft, and one additional 12 ft by 13 ft guest bedroom is included. All bedrooms have attached baths. A 7 ft by 6 ft powder room is also available. There’s a car porch for two cars and landscaped gardens at the front and back",
    metadata={"source": "10 marla single story house"},
)
document_30 = Document(
    page_content="This efficient layout includes a 14 ft by 16 ft drawing room, a 15 ft by 18 ft lounge, and a 10 ft by 14 ft kitchen with a 6 ft by 10 ft spice kitchen. The master bedroom is 14 ft by 15 ft, and the other three bedrooms measure 12 ft by 13 ft each — all with attached baths. A small powder room, laundry space, and storage area are also included. A car porch fits two vehicles, with a small front lawn.",
    metadata={"source": "10 marla single story house"},
)
document_31 = Document(
    page_content="Designed for comfort and hosting, this layout offers a 14 ft by 16 ft formal drawing room, a 12 ft by 14 ft dining area, and a spacious 16 ft by 20 ft living room. The kitchen is 10 ft by 14 ft with an adjoining 6 ft by 8 ft spice kitchen. The master bedroom is 14 ft by 16 ft, and two additional bedrooms are 12 ft by 13 ft, all with attached bathrooms. The fourth room (11 ft by 12 ft) serves as a guest bedroom or study. A powder room and laundry area are also provided. Lawn space is available at both the front and back, along with parking for two cars.",
    metadata={"source": "10 marla single story house"},
)
document_32 = Document(
    page_content="A standard 1 Kanal house is built on an approximate area of 4500 sq. ft. with a typical plot size of 50 ft by 90 ft. The suggested layout includes 5 bedrooms in total — 2 bedrooms on the ground floor (commonly for guests and parents) and 3 bedrooms on the upper floor. The drawing room measures 16 ft by 18 ft, the dining room is 14 ft by 16 ft, and the spacious living room/TV lounge is 18 ft by 22 ft. The main kitchen is 12 ft by 16 ft, complemented by an 8 ft by 10 ft dirty kitchen. There are 6 bathrooms in total, including attached baths and a powder room. A servant room with an attached bath is typically located at the rear with a separate entrance. A 10 ft by 12 ft study room or home office is included, along with a store room that may be placed on either floor. The house has a car porch suitable for 2 large cars and a spacious front and backyard. High ceilings or double-height lounges are often featured for a more luxurious appeal.",
    metadata={"source": "1 kanal house"},
)
document_33 = Document(
    page_content="This single-story design features 4 spacious bedrooms, each with attached bathrooms. The central lounge measures 18 ft by 22 ft with a double-height ceiling, creating a grand open feel. The drawing room is 16 ft by 18 ft and connects to a 14 ft by 16 ft dining area. A 12 ft by 16 ft main kitchen and 8 ft by 10 ft dirty kitchen support daily and formal cooking needs. A 10 ft by 12 ft study/home office and a rear servant room with an attached bath are also included. The car porch accommodates two large vehicles, and the front and back lawns provide ample outdoor space.",
    metadata={"source": "1 kanal single story house"},
)
document_34 = Document(
    page_content="This design includes 3 bedrooms with walk-in closets and attached baths, and a fourth room that serves as a guest or study room. The central 18 ft by 22 ft living area opens into a mini internal courtyard for ventilation and aesthetics. The 16 ft by 18 ft drawing room and 14 ft by 16 ft dining room are adjacent. The kitchen setup includes a large 12 ft by 16 ft main kitchen and an 8 ft by 10 ft spice kitchen. A servant quarter is placed separately at the back. Wide front lawn, side passages, and parking for two cars ensure comfort and compliance with building bylaws.",
    metadata={"source": "1 kanal single story house"},
)
document_35 = Document(
    page_content="This layout features 5 bedrooms, including a master bedroom of 16 ft by 18 ft, all with attached luxury baths. The lounge is 18 ft by 22 ft, with skylights or vertical windows for natural lighting. A formal drawing room and dining room maintain privacy from the living area. The kitchen includes an island in the 12 ft by 16 ft main kitchen and a connected dirty kitchen. The home office (10 ft by 12 ft) is placed near the entrance. A rear-side servant quarter, laundry room, and underground water tank area are included. Lawn wraps around three sides of the house.",
    metadata={"source": "1 kanal single story house"},
)
document_36 = Document(
    page_content="Designed for comfort and hosting, this layout offers a 14 ft by 16 ft formal drawing room, a 12 ft by 14 ft dining area, and a spacious 16 ft by 20 ft living room. The kitchen is 10 ft by 14 ft with an adjoining 6 ft by 8 ft spice kitchen. The master bedroom is 14 ft by 16 ft, and two additional bedrooms are 12 ft by 13 ft, all with attached bathrooms. The fourth room (11 ft by 12 ft) serves as a guest bedroom or study. A powder room and laundry area are also provided. Lawn space is available at both the front and back, along with parking for two cars.",
    metadata={"source": "1 kanal single story house"},
)
document_37 = Document(
    page_content="This compact but functional design includes 4 bedrooms with attached bathrooms, a 16 ft by 18 ft drawing room, and an 18 ft by 20 ft lounge. The kitchen includes a pantry and a connected dirty kitchen. A 10 ft by 12 ft study room and a ground-floor storeroom enhance utility. A separate servant room with bath is placed behind the house. A wide car porch and boundary garden complete the layout.",
    metadata={"source": "1 kanal single story house"},
)
document_38= Document(
    page_content="The ground floor includes 2 bedrooms (guest and parent) with attached baths, a 16 ft by 18 ft drawing room, and an 18 ft by 22 ft lounge. The dining room and kitchen (12 ft by 16 ft) with a dirty kitchen are connected. The upper floor contains 3 bedrooms with attached baths, a family lounge, and a study room. The servant quarter with an attached bath is placed at the rear with external access. A front-facing balcony and spacious terrace add elegance.",
    metadata={"source": "1 kanal double story house"},
)
document_39= Document(
    page_content="The ground floor includes 2 bedrooms (guest and parent) with attached baths, a 16 ft by 18 ft drawing room, and an 18 ft by 22 ft lounge. The dining room and kitchen (12 ft by 16 ft) with a dirty kitchen are connected. The upper floor contains 3 bedrooms with attached baths, a family lounge, and a study room. The servant quarter with an attached bath is placed at the rear with external access. A front-facing balcony and spacious terrace add elegance.",
    metadata={"source": "1 kanal double story house"},
)
document_40= Document(
    page_content="The ground floor includes a self-contained guest suite with separate access, ideal for privacy. The main house includes a drawing/dining area, kitchen, TV lounge, and one additional bedroom. Upstairs, 3 large bedrooms, a home office, and a second lounge offer privacy. Double-height ceilings in the entrance and lounge create openness. The servant room is accessible only from outside.",
    metadata={"source": "1 kanal double story house"},
)
document_41= Document(
    page_content="Two bedrooms are placed on the ground floor for parents and guests, along with common spaces including kitchen, lounge, and drawing room. The upper floor includes 3 bedrooms with attached baths and a kitchenette for convenience. A study room, store, and family sitting lounge complete the upper floor. The servant room is tucked away with rear access.",
    metadata={"source": "1 kanal double story house"},
)
document_42= Document(
    page_content="This minimalist layout places the master suite and one guest bedroom on the ground floor. An open-concept kitchen, dining area, and living room flow seamlessly. The upper floor includes 3 bedrooms with bathrooms, a lounge, and a home office. A rooftop terrace garden and skylight above the stair area bring in light. The servant room is placed discreetly near the rear wall",
    metadata={"source": "1 kanal double story house"},
)
document_43 = Document(
    page_content="A typical 5 Marla house usually includes 2 to 3 bedrooms, each with an attached bathroom. There is one kitchen, a TV lounge, and optionally a small drawing room. The average bedroom size is around 10 by 12 feet, the kitchen is about 6 by 8 feet, and the TV lounge is typically 12 by 14 feet.",
    )
document_44 = Document(
    page_content="A 7 Marla house generally has 3 to 4 bedrooms with attached bathrooms, a spacious TV lounge, one or two kitchens, and a drawing room. Some layouts also include a small store room. The bedrooms usually measure about 11 by 13 feet, the kitchen around 8 by 10 feet, the TV lounge is typically 14 by 16 feet, and the drawing room is around 12 by 14 feet.",
    )
document_45 = Document(
    page_content="A 10 Marla house commonly features 4 to 5 bedrooms, each with an attached bathroom, along with a large TV lounge, one or two kitchens, and a drawing and dining area, either combined or separate. Many also include a store room, and some may have a servant quarter. The average bedroom size is around 12 by 14 feet, the kitchen is 9 by 11 feet, the TV lounge is about 15 by 18 feet, the drawing room is 14 by 16 feet, and the dining room is 10 by 12 feet.",
    )
document_46 = Document(
    page_content="A 1 Kanal house usually includes 5 to 6 bedrooms, each with attached bathrooms. It typically has two TV lounges, one on each floor, and two kitchens, along with one or two drawing and dining rooms. These homes often include one or two store rooms and servant quarters, usually located at the back or in the basement. The average bedroom size is about 14 by 16 feet, the kitchen is 10 by 12 feet, the TV lounge is typically 18 by 20 feet, the drawing room is around 16 by 18 feet, and the dining room is 12 by 14 feet.",)

document_47 = Document("In a 5 Marla house, it is practical to have two bedrooms on the ground floor and one on the first floor if you opt for a double-storey design. The TV lounge often doubles as a dining area due to limited space. You can also include a small washing area or laundry space near the kitchen. The stairs are typically placed near the entrance or in the middle to optimize layout. A small car porch is usually included in the front area. If needed, a compact study nook or home office corner can be created in a hallway or extra space under the stairs.")

document_48 = Document("In a 7 Marla house, you can comfortably have two bedrooms on the ground floor and two on the upper floor. There is often space for a dedicated dining room separate from the lounge. Some designs incorporate a powder room near the entrance for guests. The house can also include a small terrace on the first floor. If you plan for a modern design, an open kitchen with a breakfast counter connected to the lounge is a popular choice. A small storage space under the stairs or a pantry room can also be added for convenience.")

document_49 = Document("A 10 Marla house usually allows for two spacious bedrooms on each floor, with the possibility of a fifth room as a guest room or study. The drawing and dining rooms are usually separated from the lounge to provide privacy for guests. It’s common to have a powder room, a laundry area, and a store room on the ground floor. With a bigger backyard, you can have a patio or small garden area, and even a barbecue zone. An upper-floor terrace can serve as a relaxing outdoor space. The main kitchen is on the ground floor, while a secondary kitchenette is sometimes added upstairs.")
document_50 = Document("In a 1 Kanal house, you have the space for three bedrooms on the ground floor and three more on the upper floor. Each bedroom can have a walk-in closet, and bathrooms can include bathtubs or shower cabins. The ground floor usually includes a formal drawing room and a separate formal dining room, in addition to the TV lounge. A home office, gym room, or even a small library can be added. The house usually has a laundry room, servant quarters, a pantry, and ample storage rooms. A spacious car porch or garage for 2–3 cars is standard. Outdoor areas may include a garden, patio, or even a small swimming pool depending on the layout.")
document_51 = Document("A typical 5 Marla house includes 2 to 3 bedrooms, each measuring around 10x12 feet, with attached bathrooms of about 5x7 feet. There is 1 TV lounge (approximately 12x14 feet), 1 kitchen (around 6x8 feet), and usually 1 drawing room (10x12 feet). A powder room of 4x5 feet can be added near the entrance. There may also be 1 small store room of 5x5 feet and a washing area of 4x6 feet. A compact car porch of 10x12 feet usually fits one car. In total, the house may contain 7 to 8 rooms, including bedrooms, kitchen, lounge, and utility spaces")
document_52 = Document("A 7 Marla house generally has 3 to 4 bedrooms, each around 11x13 feet, with attached bathrooms of 6x8 feet. It includes 1 spacious TV lounge (14x16 feet), 1 or 2 kitchens (main kitchen around 8x10 feet), and 1 drawing room (12x14 feet). Some designs also feature 1 dining room (10x12 feet), 1 powder room (4x6 feet), and a small laundry room (6x8 feet). A study room of 8x10 feet can be added on the first floor. A balcony or terrace measuring 6x10 feet is also common. Altogether, the house contains 9 to 10 rooms.")
document_53 = Document("In a 10 Marla house, there are usually 4 to 5 bedrooms (each around 12x14 feet) with attached baths (7x9 feet), 2 TV lounges (main lounge 15x18 feet), and 1 or 2 kitchens (9x11 feet). The house also includes 1 drawing room (14x16 feet), 1 dining room (10x12 feet), and 1 powder room (5x6 feet). You’ll also find a laundry room (8x10 feet), 1 store room (6x8 feet), and an optional guest room or study (10x12 feet). Many homes include a servant quarter (8x10 feet) at the rear. Overall, the house comprises 11 to 13 rooms.")
document_54 = Document("A 1 Kanal house typically consists of 5 to 6 spacious bedrooms, each around 14x16 feet, with attached bathrooms of 8x10 feet and walk-in closets (8x10 feet). There are usually 2 TV lounges (18x20 feet), 2 kitchens (10x12 feet), 1 formal drawing room (16x18 feet), and 1 dining room (12x14 feet). You may also find 1 study room (10x12 feet), 1 home office or library (10x14 feet), and 1 powder room (5x6 feet). Utility areas include 1 laundry room (10x12 feet), 1 or 2 servant quarters (10x12 feet), and 1 storeroom (8x10 feet). A garage or car porch measuring 16x20 feet typically accommodates 2 vehicles. Altogether, the house can have 14 to 18 rooms, depending on the layout.")






documents = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
    document_11,
    document_12,
    document_13,
    document_14,
    document_15,
    document_16,
    document_17,
    document_18,
    document_19,
    document_20,
    document_21,
    document_22,
    document_23,
    document_24,
    document_25,
    document_26,
    document_27,
    document_28,
    document_29,
    document_30,
    document_31,
    document_32,
    document_33,
    document_34,
    document_35,
    document_36,
    document_37,
    document_38,
    document_39,
    document_40,
    document_41,
    document_42,
    document_43,
    document_44,
    document_45,
    document_46,
    document_47,
    document_48,
    document_49,
    document_50,
    document_51,
    document_52,
    document_53,
    document_54,
    

    

]
uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, ids=uuids)
