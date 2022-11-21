@app.get('/name/{name}')
async def read_name(name: str):
	for mahasiswa_item in data['DataNIM']:
		name = mahasiswa_item['NamaMahasiswa']
		if name.split(' ').pop(0) == name:
			return mahasiswa_item
	raise HTTPException(
		status_code=404, detail=f'Item not found')