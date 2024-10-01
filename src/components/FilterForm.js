import React, { useState } from 'react';
import { TextField, Button, MenuItem, Box } from '@mui/material';

const FormComponent = () => {
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [fieldNameValue, setFieldNameValue] = useState('');
    const [fieldValue, setFieldValue] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        $('#loader').show();
        $('#data-table-root').hide();
        $('#button-container').hide();

        const formData = {
            startDate,
            endDate,
            fieldNameValue,
            fieldValue,
        };

        const response = await fetch('/submit-filter-form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            const filteredRecords = await response.json();
            if (filteredRecords.length === 0) {
                clearTable();
            } else {
                updateTable(filteredRecords);
            }
            console.log('Form submitted successfully');
        } else {
            console.error('Form submission failed');
            alert('Something went wrong. Please try again!');
        }
        $('#loader').hide();
        $('#data-table-root').show();
        $('#button-container').show();
    };

    const updateTable = (records) => {
        const table = $('#records-table').DataTable();
        table.clear();
        records.forEach(record => {
            table.row.add([
                record._id,
                record.originationTime,
                record.clusterId,
                record.userId,
                record.devices.phone,
                record.devices.voicemail
            ]).draw();
        });
    };

    const clearTable = () => {
        const table = $('#records-table').DataTable();
        table.clear().draw();
    };

    return (
        <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
            <TextField
                label="Start Date"
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                InputLabelProps={{ shrink: true }}
                sx={{ minWidth: 200 }}
                required
            />
            <TextField
                label="End Date"
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                InputLabelProps={{ shrink: true }}
                sx={{ minWidth: 200 }}
                required
            />
            <TextField
                label="Select Field Name"
                select
                value={fieldNameValue}
                onChange={(e) => setFieldNameValue(e.target.value)}
                sx={{ minWidth: 200 }}
            >
                <MenuItem value="">Select an option</MenuItem>
                <MenuItem value="phoneNumber">Phone Number</MenuItem>
                <MenuItem value="email">Email</MenuItem>
                <MenuItem value="address">Address</MenuItem>
            </TextField>
            <TextField
                label="Input Box"
                value={fieldValue}
                onChange={(e) => setFieldValue(e.target.value)}
                sx={{ minWidth: 200 }}
            />
            <Button type="submit" variant="contained" color="primary">
                Submit
            </Button>
        </Box>
    );
};

export default FormComponent;