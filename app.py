{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f851f19a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [04/Oct/2023 20:32:59] \"GET / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/', methods=['GET'])\n",
    "def index():\n",
    "    return \"Welcome to the Outpatient Appointment System!\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='127.0.0.1', port=5000)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1888c34c",
   "metadata": {},
   "outputs": [],
   "source": [
    "doctors = [\n",
    "    {\n",
    "        \"id\": 1,\n",
    "        \"name\": \"Dr. Smith\",\n",
    "        \"specialty\": \"General Physician\",\n",
    "        \"max_patients_per_day\": 10,\n",
    "    },\n",
    "    # Add more doctors\n",
    "]\n",
    "\n",
    "appointments = []\n",
    "\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "536e37d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/api/doctors', methods=['GET'])\n",
    "def get_doctors():\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "485806c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/api/doctors/<int:doctor_id>', methods=['GET'])\n",
    "def get_doctor(doctor_id):\n",
    "    doctor = next((doc for doc in doctors if doc['id'] == doctor_id), None)\n",
    "    if doctor:\n",
    "        return jsonify(doctor)\n",
    "    return jsonify({\"message\": \"Doctor not found\"}), 404\n",
    "\n",
    "# ...\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfce653d",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/api/appointments', methods=['POST'])\n",
    "def book_appointment():\n",
    "    data = request.get_json()\n",
    "\n",
    "    # Check if doctor exists\n",
    "    doctor = next((doc for doc in doctors if doc['id'] == data['doctor_id']), None)\n",
    "    if not doctor:\n",
    "        return jsonify({\"message\": \"Doctor not found\"}), 404\n",
    "\n",
    "    # Check if the doctor has available slots\n",
    "    # Implement logic to check evenings and max patients per day here\n",
    "    # ...\n",
    "\n",
    "    # Create appointment\n",
    "    appointment = {\n",
    "        \"doctor_id\": data['doctor_id'],\n",
    "        \"patient_name\": data['patient_name'],\n",
    "        \"date\": data['date'],\n",
    "        \"time_slot\": data['time_slot'],\n",
    "    }\n",
    "    appointments.append(appointment)\n",
    "    return jsonify({\"message\": \"Appointment booked successfully\"})\n",
    "\n",
    "# ...\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "739b94ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f1f0d41",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f50811ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7dbc9a7e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89857b7b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e217568f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
