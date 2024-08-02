import streamlit as st
import pandas as pd
import pickle

# Title
st.title('🏩🌳 Real Estate Price Prediction')

def load_model():
    model = pickle.load(open('randomforest_model.pkl', 'rb'))
    return model

st.write('Please fill in the following fields to get the price prediction of the property.')

st.write('---')

#defining the values for the categorical columns
sorted_peb = {
    'B': 1,
    'D': 2,
    'F': 3,
    'E': 4,
    'A': 5,
    'C': 6,
    'G': 7,
    'A++': 8,
    'A+': 9,
    'B_A': 10,
    'A_A+': 11,
    'E_D': 12,
    'E_C': 13,
    'F_C': 14,
    'F_D': 15,
    'G_C': 16,
    'F_E': 17
}


sorted_district = {
    'Brugge': 1,           
    'Tournai': 2,         
    'Veurne': 1,             
    'Hasselt': 3,         
    'Brussels': 4,        
    'Mechelen': 5,          
    'Halle-Vilvoorde': 6,    
    'Sint-Niklaas': 7,     
    'Oostend': 1,            
    'Ieper': 1,            
    'Mons': 2,             
    'Namur': 8,            
    'Leuven': 6,            
    'Antwerp': 5,           
    'Nivelles': 9,          
    'Charleroi': 2,         
    'Liège': 10,            
    'Maaseik': 3,           
    'Verviers': 10,        
    'Aalst': 7,              
    'Soignies': 2,         
    'Tongeren': 3,           
    'Marche-en-Famenne': 11,  
    'Kortrijk': 1,           
    'Gent': 7,             
    'Eeklo': 7,           
    'Diksmuide': 1,         
    'Dendermonde': 7,       
    'Waremme': 10,        
    'Philippeville': 8,      
    'Huy': 10,               
    'Dinant': 8,             
    'Neufchâteau': 11,        
    'Mouscron': 2,           
    'Tielt': 1,               
    'Roeselare': 1,          
    'Turnhout': 5,            
    'Oudenaarde': 7,       
    'Thuin': 2,           
    'Arlon': 11,          
    'Virton': 11,           
    'Ath': 2,             
    'Bastogne': 11           
}


sorted_province = {
    'West Flanders': 1,
    'Hainaut': 2,
    'Limburg': 3,
    'Brussels': 4,
    'Antwerp': 5,
    'Flemish Brabant': 6,
    'East Flanders': 7,
    'Namur': 8,
    'Walloon Brabant': 9,
    'Liège': 10,
    'Luxembourg': 11
}


sorted_region = {
    'Flanders': 1,
    'Wallonie': 2,
    'Brussels': 3
}

sorted_subtypeofproperty = {
    'Flat Studio': 1, 
    'Apartment': 2, 
    'Service Flat': 3,
    'Kot': 4,
    'Ground Floor': 5,
    'House': 6,
    'Loft': 7,
    'Duplex': 8, 
    'Triplex': 9, 
    'Town House': 10, 
    'Bungalow': 11, 
    'Apartment Block': 12, 
    'Mixed Use Building': 13, 
    'Penthouse': 14, 
    'Chalet': 15, 
    'Country Cottage': 16, 
    'Farmhouse': 17, 
    'Villa': 18, 
    'Manor House': 19, 
    'Mansion': 20, 
    'Castle': 21, 
    'Pavilion': 22,
    'Exceptional Property': 23,
    'Other Property': 24


}

sorted_floodingzone = {
    'No Flood Zone': 0,
    'Possible Flood Zone': 1,
    'Waterside Zone': 2,
    'Flood Zone': 3,
    'Possible Non-Circumscribed Flood Zone': 4,
    'Recognized Flood Zone': 5,
    'Recognized Non-Circumscribed Flood Zone': 6,
    'Recognized Waterside Flood Zone': 7,
    'Possible Non-Circumscribed Waterside Zone': 8
}

sorted_kitchen = {
    ' Not Installed': 0,   
    'Installed': 1,            
    'Semi-Equipped': 2,         
    'Hyper-Equipped': 3       
}

sorted_typeofsale = {
    'Residential Sale': 1,

}

sorted_country = {
    'Belgium': 1
}

sorted_typeofproperty= {
    'House': 1,
    'Apartment': 2,
}

sorted_stateofbuilding = {
    'Good': 1,
    'As New': 2,
    'Just Renovated': 3,
    'To Renovate': 4,
    'To Be Done Up': 5,
    'To Restore': 6
}

sorted_numberoffacades = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
}



# Check if 'prediction_price' is not yet in the session state
if 'prediction_price' not in st.session_state:
    
# If not, create an empty list
    st.session_state.prediction_price = []



# Define user input
user_input = {
    "bathroomcount": st.select_slider('🚿 Bathroom Count',options=list(range(1, 7)), key='bathroomcount'),}
st.markdown("---")

user_input["bedroomcount"] = st.select_slider('🛏️ Bedroom Count', options=list(range(1, 10)), key='bedroomcount')
st.markdown("---")

user_input["constructionyear"] = st.number_input('🏠 Construction Year', min_value=1800, max_value=2026, key='constructionyear')
st.markdown("---")

user_input["country"] = sorted_country[st.radio('🗺️ Country', list(sorted_country.keys()), key='country')]
st.markdown("---")

user_input["district"] = sorted_district[st.selectbox('📍 District', list(sorted_district.keys()), key='district')]
st.markdown("---")

user_input["fireplace"] = st.checkbox('🔥 Fireplace', key='fireplace')
st.markdown("---")

user_input["floodingzone"] = sorted_floodingzone[st.selectbox('🌊 Flooding Zone', list(sorted_floodingzone.keys()), key='floodingzone')]
st.markdown("---")

user_input["furnished"] = st.checkbox('🛋️ Furnished', key='furnished')
st.markdown("---")

user_input["garden"] = st.checkbox('🌳 Garden', key='garden')
st.markdown("---")

user_input["kitchen"] = sorted_kitchen[st.radio('🍽️ Kitchen', list(sorted_kitchen.keys()),horizontal=True,key='kitchen')]
st.markdown("---")

user_input["livingarea"] = st.number_input('📐 Living Area (sqm)', min_value=0, key='livingarea')
st.markdown("---")

user_input["monthlycharges"] = st.number_input('💵 Monthly Charges', min_value=0, key='monthlycharges')
st.markdown("---")

user_input["numberoffacades"] = sorted_numberoffacades[st.radio('🏠 Number of Facades', list(sorted_numberoffacades.keys()),horizontal=True, key='numberoffacades')]
st.markdown("---")

user_input["peb"] = sorted_peb[st.selectbox('⚡ Energy Performance', list(sorted_peb.keys()), key='sorted_peb')]
st.markdown("---")

user_input["province"] = sorted_province[st.selectbox('🌍 Province', list(sorted_province.keys()), key='province')]
st.markdown("---")

user_input["region"] = sorted_region[st.radio('🌐 Region', list(sorted_region.keys()), key='region')]
st.markdown("---")

user_input["roomcount"] = st.select_slider('🛋️ Room Count', options=list(range(1, 32)), key='roomcount')
st.markdown("---")

user_input["showercount"] = st.select_slider('🚿 Shower Count', options=[1, 2, 3, 4, 5, 6], key='showercount')
st.markdown("---")

user_input["stateofbuilding"] = sorted_stateofbuilding[st.selectbox('🏛️ State of Building', list(sorted_stateofbuilding.keys()), key='stateofbuilding')]
st.markdown("---")

user_input["subtypeofproperty"] = sorted_subtypeofproperty[st.selectbox('🏰 Subtype of Property', list(sorted_subtypeofproperty.keys()), key='subtypeofproperty')]
st.markdown("---")

user_input["surfaceofplot"] = st.number_input('📏 Surface of Plot (sqm)', min_value=0, key='surfaceofplot')
st.markdown("---")

user_input["swimmingpool"] = st.checkbox('🏊 Swimming Pool', key='swimmingpool')
st.markdown("---")

user_input["terrace"] = st.checkbox('🏖️ Terrace', key='terrace')

st.markdown("---")

user_input["toiletcount"] = st.select_slider('🚽 Toilet Count', options=[1, 2, 3, 4, 5, 6], key='toiletcount')
st.markdown("---")

user_input["typeofproperty"] = sorted_typeofproperty[st.radio('🏠/🏢 Type of Property', list(sorted_typeofproperty.keys()), key='typeofproperty')]
st.markdown("---")

user_input["typeofsale"] = sorted_typeofsale[st.radio('🍽️ Type of Sale', list(sorted_typeofsale.keys()), key='typeofsale')]
st.markdown("---")




# Model prediction
model = load_model()

if st.button("🔮 Predict"):
    user_input_df = pd.DataFrame([user_input])
    prediction = model.predict(user_input_df)
    
    prediction_price = f"€{prediction[0]:.2f}"
    st.session_state.prediction_price.append({'Input': user_input, 'Prediction': prediction_price})
    
    # Display the prediction result in a table format
    st.write(f"💰 **Predicted Price:** {prediction_price}")
    st.markdown("---")
    st.success('Prediction successful!')
    st.balloons()

    # Prepare the data for tabular display
    result_df = pd.DataFrame([user_input])
    result_df['Predicted Price'] = prediction_price

    st.write("📈 **Previous Predictions:**")
    st.write(result_df)

    if not st.session_state.prediction_price:
        st.write("📈 No Previous Predictions")
    else:
        st.write("📈 **All Previous Predictions:**")
        all_predictions_df = pd.DataFrame(st.session_state.prediction_price)
        st.write(all_predictions_df)
        