from flask import Blueprint, jsonify, request
from app.controllers.members_controller import MembersController

members_blueprint = Blueprint('members', __name__)

# route to add members
@members_blueprint.route('/members', methods=['POST'])
def add_member():
    required_fields = ['member_identification_id']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_identification_id = data['member_identification_id']

    # Call controller method to add user
    new_member = MembersController.add_member(member_identification_id)
    
    if new_member:
        return jsonify({'message': 'Member added successfully', 'member': new_member, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member', 'status_code': 500}), 200
 
 
 
 
# route to add member profile details
@members_blueprint.route('/members/profile', methods=['POST'])
def add_member_profile_details():
    required_fields = ['member_id', 'member_image', 'prefix', 'first_name', 'last_name', 'other_names', 'gender', 'date_of_birth', 'place_of_birth', 'home_town', 'nationality', 'highest_level_of_education', 'institution_of_education', 'status_of_education', 'profession', 'employment_status', 'institution_of_employment', 'medical_conditions', 'mortality_status']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    member_image = data['member_image']
    prefix = data['prefix']
    first_name = data['first_name']
    last_name = data['last_name']
    other_names = data['other_names']
    gender = data['gender']
    date_of_birth = data['date_of_birth']
    place_of_birth = data['place_of_birth']
    home_town = data['home_town']
    nationality = data['nationality']
    highest_level_of_education = data['highest_level_of_education']
    institution_of_education = data['institution_of_education']
    status_of_education = data['status_of_education']
    profession = data['profession']
    employment_status = data['employment_status']
    institution_of_employment = data['institution_of_employment']
    medical_conditions = data['medical_conditions']
    mortality_status = data['mortality_status']

    # Call controller method to add user
    new_member_profile_detail = MembersController.add_member_profile_details(member_id, member_image, prefix, first_name, last_name, other_names, gender, date_of_birth, place_of_birth, home_town, nationality, highest_level_of_education, institution_of_education, status_of_education, profession, employment_status, institution_of_employment, medical_conditions, mortality_status)
    
    if new_member_profile_detail:
        return jsonify({'message': 'Member Profile details added successfully', 'member_profile': new_member_profile_detail, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member profile details', 'status_code': 500}), 200 




# route to add member marriage and family details
@members_blueprint.route('/members/family_and_marriage', methods=['POST'])
def add_member_family_and_marriage_details():
    required_fields = ['member_id', 'marital_status', 'marriage_type', 'date_of_marriage', 'officiating_minister', 'place_of_marriage', 'marriage_license_number', 'fathers_name', 'fathers_phone_number', 'fathers_membership_status', 'fathers_mortality_status', 'mothers_name', 'mothers_phone_number', 'mothers_membership_status', 'mothers_mortality_status', 'spouse_name', 'spouse_phone', 'spouse_membership_status', 'spouse_mortality_status']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    marital_status = data['marital_status']
    marriage_type = data['marriage_type']
    date_of_marriage = data['date_of_marriage']
    officiating_minister = data['officiating_minister']
    place_of_marriage = data['place_of_marriage']
    marriage_license_number = data['marriage_license_number']
    fathers_name = data['fathers_name']
    fathers_phone_number = data['fathers_phone_number']
    fathers_membership_status = data['fathers_membership_status']
    fathers_mortality_status = data['fathers_mortality_status']
    mothers_name = data['mothers_name']
    mothers_phone_number = data['mothers_phone_number']
    mothers_membership_status = data['mothers_membership_status']
    mothers_mortality_status = data['mothers_mortality_status']
    spouse_name = data['spouse_name']
    spouse_phone = data['spouse_phone']
    spouse_membership_status = data['spouse_membership_status']
    spouse_mortality_status = data['spouse_mortality_status']
    


    # Call controller method to add  member marriage and family details
    new_member_family_and_marriage_details = MembersController.add_member_family_and_marriage_details(member_id, marital_status, marriage_type, date_of_marriage, officiating_minister, place_of_marriage, marriage_license_number, fathers_name, fathers_phone_number, fathers_membership_status, fathers_mortality_status, mothers_name, mothers_phone_number, mothers_membership_status, mothers_mortality_status, spouse_name, spouse_phone, spouse_membership_status, spouse_mortality_status)
    
    if new_member_family_and_marriage_details:
        return jsonify({'message': 'Member Family And Marriage details added successfully', 'member_family_and_marriage': new_member_family_and_marriage_details, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member family and marriage details', 'status_code': 500}), 200 



# route to add member member children detail
@members_blueprint.route('/members/children', methods=['POST'])
def add_member_children_details():
    required_fields = ['member_id', 'child_name', 'child_phone_number']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    child_name = data['child_name']
    child_phone_number = data['child_phone_number']

    # Call controller method to add  member children detail
    new_member_children_details = MembersController.add_member_children_details(member_id, child_name, child_phone_number)
    
    if new_member_children_details:
        return jsonify({'message': 'Member Children details added successfully', 'member_children': new_member_children_details, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member children details', 'status_code': 500}), 200 



# route to add member contact details
@members_blueprint.route('/members/contact', methods=['POST'])
def add_member_contact_details():
    required_fields = ['member_id', 'phone_number', 'email', 'residential_address', 'postal_address', 'place_of_residence', 'closest_landmark']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    phone_number = data['phone_number']
    email = data['email']
    residential_address = data['residential_address']
    postal_address = data['postal_address']
    place_of_residence = data['place_of_residence']
    closest_landmark = data['closest_landmark']

    # Call controller method to add  member contact details
    new_member_contact_details = MembersController.add_member_contact_details(member_id, phone_number, email, residential_address, postal_address, place_of_residence, closest_landmark)
    
    if new_member_contact_details:
        return jsonify({'message': 'Member Contact details added successfully', 'member_contact': new_member_contact_details, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member contact details', 'status_code': 500}), 200



# route to add member church details
@members_blueprint.route('/members/church', methods=['POST'])
def add_member_church_details():
    required_fields = ['member_id', 'department', 'areas_of_ministry', 'professional_service', 'member_status', 'water_baptism_date', 'place_of_baptism', 'officiating_minister', 'water_baptism_certificate_number', 'holy_spirit_baptism_status', 'member_since', 'transferred_from']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    department = data['department']
    areas_of_ministry = data['areas_of_ministry']
    professional_service = data['professional_service']
    member_status = data['member_status']
    water_baptism_date = data['water_baptism_date']
    place_of_baptism = data['place_of_baptism']
    officiating_minister = data['officiating_minister']
    water_baptism_certificate_number = data['water_baptism_certificate_number']
    holy_spirit_baptism_status = data['holy_spirit_baptism_status']
    member_since = data['member_since']
    transferred_from = data['transferred_from']

    # Call controller method to add  member church details
    new_member_church_details = MembersController.add_member_church_details(member_id, department, areas_of_ministry, professional_service, member_status, water_baptism_date, place_of_baptism, officiating_minister, water_baptism_certificate_number, holy_spirit_baptism_status, member_since, transferred_from)
    
    if new_member_church_details:
        return jsonify({'message': 'Member Church details added successfully', 'member_church': new_member_church_details, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member church details', 'status_code': 500}), 200




# route to add member special note
@members_blueprint.route('/members/special_notes', methods=['POST'])
def add_member_special_note():
    required_fields = ['member_id', 'special_note']
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 200
    
    member_id = data['member_id']
    special_note = data['special_note']

    # Call controller method to add  member special note
    new_member_special_note = MembersController.add_member_special_note(member_id, special_note)
    
    if new_member_special_note:
        return jsonify({'message': 'Member Special Note added successfully', 'member_special_note': new_member_special_note, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add member special note', 'status_code': 500}), 200



# Route to fetch last inserted member
@members_blueprint.route('/recent/member', methods=['GET'])
def get_last_inserted_profile():
    member = MembersController.get_last_inserted_member()
    if member:
        return jsonify({'member': {'id': member[0], 'member_identification_id': member[1]}, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Members table is empty', 'status_code': 404}), 404
    

# Route to fetch all members
@members_blueprint.route('/members', methods=['GET'])
def get_members():    
    members = MembersController.get_all_members()
    
    formatted_members = []
    for member in members:
        formatted_members.append({
            'id': member[0],
            'member_identification_id': member[1],
            'member_image': member[2],
            'prefix': member[3],
            'first_name': member[4],
            'last_name': member[5],
            'other_names': member[6],
            'gender': member[7],
            'date_of_birth': member[8],
            'place_of_birth': member[9],
            'home_town': member[10],
            'nationality': member[11],
            'highest_level_of_education': member[12],
            'institution_of_education': member[13],
            'status_of_education': member[14],
            'profession': member[15],
            'employment_status': member[16],
            'institution_of_employment': member[17],
            'medical_conditions': member[18],
            'mortality_status': member[19],
            'marital_status': member[20],
            'marriage_type': member[21],
            'date_of_marriage': member[22],
            'officiating_minister': member[23],
            'place_of_marriage': member[24],
            'marriage_license_number': member[25],
            'fathers_name': member[26],
            'fathers_phone_number': member[27],
            'fathers_membership_status': member[28],
            'fathers_mortality_status': member[29],
            'mothers_name': member[30],
            'mothers_phone_number': member[31],
            'mothers_membership_status': member[32],
            'mothers_mortality_status': member[33],
            'spouse_name': member[34],
            'spouse_phone': member[35],
            'spouse_membership_status': member[36],
            'spouse_mortality_status': member[37],
            'child_name': member[38],
            'child_phone_number': member[39],
            'phone_number': member[40],
            'email': member[41],
            'residential_address': member[42],
            'postal_address': member[43],
            'place_of_residence': member[44],
            'closest_landmark': member[45],
            'department': member[46],
            'areas_of_ministry': member[47],
            'professional_service': member[48],
            'member_status': member[49],
            'water_baptism_date': member[50],
            'place_of_baptism': member[51],
            'officiating_minister': member[52],
            'water_baptism_certificate_number': member[53],
            'holy_spirit_baptism_status': member[54],
            'member_since': member[55],
            'transferred_from': member[56],
            'special_note': member[57],
            'inserted_at': member[58],
            'updated_at': member[59]
        })
    
    return jsonify({'members': formatted_members})


# Route to fetch a specific member by ID
@members_blueprint.route('/members/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):    
    member = MembersController.get_member_by_id(member_id)

    if member:
            return jsonify({'member': {
                'id': member[0],
                'member_identification_id': member[1],
                'member_image': member[2],
                'prefix': member[3],
                'first_name': member[4],
                'last_name': member[5],
                'other_names': member[6],
                'gender': member[7],
                'date_of_birth': member[8],
                'place_of_birth': member[9],
                'home_town': member[10],
                'nationality': member[11],
                'highest_level_of_education': member[12],
                'institution_of_education': member[13],
                'status_of_education': member[14],
                'profession': member[15],
                'employment_status': member[16],
                'institution_of_employment': member[17],
                'medical_conditions': member[18],
                'mortality_status': member[19],
                'marital_status': member[20],
                'marriage_type': member[21],
                'date_of_marriage': member[22],
                'officiating_minister': member[23],
                'place_of_marriage': member[24],
                'marriage_license_number': member[25],
                'fathers_name': member[26],
                'fathers_phone_number': member[27],
                'fathers_membership_status': member[28],
                'fathers_mortality_status': member[29],
                'mothers_name': member[30],
                'mothers_phone_number': member[31],
                'mothers_membership_status': member[32],
                'mothers_mortality_status': member[33],
                'spouse_name': member[34],
                'spouse_phone': member[35],
                'spouse_membership_status': member[36],
                'spouse_mortality_status': member[37],
                'child_name': member[38],
                'child_phone_number': member[39],
                'phone_number': member[40],
                'email': member[41],
                'residential_address': member[42],
                'postal_address': member[43],
                'place_of_residence': member[44],
                'closest_landmark': member[45],
                'department': member[46],
                'areas_of_ministry': member[47],
                'professional_service': member[48],
                'member_status': member[49],
                'water_baptism_date': member[50],
                'place_of_baptism': member[51],
                'officiating_minister': member[52],
                'water_baptism_certificate_number': member[53],
                'holy_spirit_baptism_status': member[54],
                'member_since': member[55],
                'transferred_from': member[56],
                'special_note': member[57],
                'inserted_at': member[58],
                'updated_at': member[59]
           }, 'status_code': 200  }), 200
            
    else:
        return jsonify({'error': 'Member not found', 'status_code': 404}), 404