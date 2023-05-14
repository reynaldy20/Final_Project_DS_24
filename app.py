import streamlit as st
import pickle
from PIL import Image

def main():
    background="""  <div style='background-color:#2a3b9c; padding:13px'>
                    <h1 style='color:white'>Model Deployment hotel customer booking status</h1>
                    <h2 style='color:white'>By: Rasyadan, Firmania, Adhea, Reynaldy</h2>
                    </div> """
    st.markdown(background,unsafe_allow_html=True)
    left,right=st.columns((2,2))
    customer = left.number_input('Total Customer',value=0)
    weekend_night = right.number_input('Weekend Night',value=0)
    week_night = left.number_input('Week Night',value=0)
    meal_type = right.selectbox('Meal Type',('Not Selected','Meal Plan 1','Meal Plan 2','Meal Plan 3'))
    car_parking = left.selectbox('Require Parking Car',('Yes','No'))
    room_type = right.selectbox('Room Type',('RoomType1','RoomType2','RoomType3','RoomType4','RoomType5','RoomType6','RoomType7'))
    lead = left.number_input('Lead Time',value=0)
    market_segment = right.selectbox('Market Segment',('Aviation','Complementary','Corporate','Offline','Online'))
    repeated_guest = left.selectbox('Repeated Guest',('Yes','No'))
    previous_cancel = right.number_input('Total Previous Canceled',value=0)
    previous_booking = left.number_input('Total Previous Booking',value=0)
    avg_price = right.number_input('Average Price Per Room')
    special_guest = left.number_input('Total Special Guest',value=0)
    button = st.button('Predict')
    if meal_type == 'Not Selected':
        meal = 3
    elif meal_type == 'Meal Plan 1':
        meal = 0
    elif meal_type == 'Meal Plan 2':
        meal=1
    else :
        meal=2
    park = 0 if car_parking == 'No' else 1
    room = 0 if room_type == 'RoomType1' else 1 if room_type == 'RoomType2' else 2 if room_type == 'RoomType3' else 3 if room_type == 'RoomType4' else 4 if room_type == 'RoomType5' else 5 if room_type == 'RoomType6' else 6
    market = 0 if market_segment == 'Aviation' else 1 if market_segment == 'Complementary' else 2 if market_segment == 'Corporate' else 3 if market_segment == 'Offline' else 4
    rep = 0 if repeated_guest == 'No' else 1
    if button:
        result=pred(customer,weekend_night,week_night,meal,park,room,lead,market,rep,
                    previous_cancel,previous_booking,avg_price,special_guest)
        if result == 'Not Cancel':
            img_not_cancel = Image.open('Image/Not Cancel.png')
            st.image(img_not_cancel)
            st.success(f'This Customer Will {result} his reservation')
        else:
            img_cancel = Image.open('Image/Cancel.png')
            st.image(img_cancel)
            st.success(f'This Customer Will {result} his reservation')


with open('Model/random_forest_mode.pkl','rb') as file1:
    rf_model = pickle.load(file1)

def pred(customer,weekend_night,week_night,meal,park,room,lead,market,rep,
        previous_cancel,previous_booking,avg_price,special_guest):
    prediction = rf_model.predict([[customer,weekend_night,week_night,meal,park,room,lead,market,rep,
                                  previous_cancel,previous_booking,avg_price,special_guest]])
    verdict = "Cancel" if prediction==0 else "Not Cancel"

    return verdict


if __name__=="__main__":
    main()