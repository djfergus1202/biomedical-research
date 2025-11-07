# BioMed Research Suite v3.0 Pro

> *Professional Integrated Computational Biology Platform*

A comprehensive drug discovery platform combining molecular docking, efficacy prediction, and cell dynamics in one seamless workflow.

---

## 🌟 What's Included

### **Option 1: Pro Version (Recommended)** 
`biomed_suite_pro.html` - **NEW v3.0**

Complete integrated workflow with:
- ✅ 3-step guided drug discovery pipeline
- ✅ Molecular docking analysis
- ✅ Drug efficacy prediction
- ✅ Cell culture simulation
- ✅ Advanced ADMET analysis
- ✅ Export to JSON/CSV/Complete Reports
- ✅ Professional animations and UI

### **Option 2: Basic Version**
`unified_biomedical_suite.html` - v2.0

Simple tab-based interface with:
- ✅ Molecular docking module
- ✅ Cell dynamics module
- ✅ Basic visualizations
- ✅ Straightforward workflow

**Both versions use the same backend:** `unified_backend.py`

---

## 🚀 Quick Start (3 Minutes)

### Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Validate system (optional)
python validate_system.py

# 3. Start backend
python unified_backend.py
# Server starts at http://127.0.0.1:5000

# 4. Open frontend in browser
# PRO: biomed_suite_pro.html
# BASIC: unified_biomedical_suite.html
```

### Cloud Deployment

#### Render.com (Recommended)
1. Create GitHub repository with all files
2. Go to [render.com](https://render.com) → Sign up/Login
3. Click **"New +"** → **"Blueprint"**
4. Connect your GitHub repo
5. Render auto-deploys using `render.yaml`
6. Access at: `https://your-app.onrender.com`

#### Heroku
```bash
# 1. Create app
heroku create your-app-name

# 2. Deploy
git add .
git commit -m "Deploy BioMed Suite"
git push heroku main

# 3. Open
heroku open
```

---

## 🧬 Features Overview

### 🔬 Molecular Docking
**Predict protein-ligand binding**
- Multiple binding mode generation (9 poses)
- Binding affinity scoring (kcal/mol)
- Interaction analysis (H-bonds, hydrophobic, π-π)
- Binding site characterization
- RMSD calculations

**Supported Targets:**
- HIV-1 Protease (1HVH)
- Cyclooxygenase-2 (2OXY)
- SARS-CoV-2 Main Protease (6LU7)
- EGFR Kinase (5R81)
- μ-opioid receptor (4DKL)

**Ligand Library:**
- Aspirin, Ibuprofen (NSAIDs)
- Morphine (Opioid)
- Remdesivir (Antiviral)
- Dexamethasone (Corticosteroid)
- Gefitinib (Tyrosine Kinase Inhibitor)

### 🎯 Drug Efficacy Prediction *(Pro Only)*
**Calculate drug potency**
- IC50 estimation from binding affinity
- Dose-response curve modeling
- Concentration optimization
- Efficacy scoring (% cell kill)
- Viability prediction

### 🧫 Cell Culture Simulation
**Real-time cell dynamics**
- Live visualization (800×600 μm field)
- Growth curve analysis
- Viability tracking
- Cell cycle phases (G1/S/G2/M)
- Drug effect visualization
- Metabolic monitoring

**Cell Lines:**
- HeLa (Cervical cancer)
- MCF-7 (Breast cancer - ER+)
- A549 (Lung cancer - KRAS mutant)
- HEK293 (Embryonic kidney - normal)

### 📊 ADMET Analysis *(Pro Enhanced)*
**Drug-like properties**
- **Absorption:** Intestinal absorption, Caco-2, bioavailability
- **Distribution:** Volume, BBB penetration, plasma binding
- **Metabolism:** CYP450 interactions, half-life
- **Excretion:** Clearance rates
- **Toxicity:** Ames test, hERG, hepatotoxicity

### 💾 Export & Reporting *(Pro Enhanced)*
- **JSON:** Full structured data
- **CSV:** Tabular data for analysis
- **Complete Reports:** Integrated workflow results
- **Docking Results:** Binding modes and interactions
- **Simulation Data:** Time-series cell counts

---

## 📚 API Documentation

### Base URL
```
Local: http://127.0.0.1:5000
Production: https://your-app.onrender.com
```

### Endpoints

#### Health Check
```http
GET /api/health
```
**Response:**
```json
{
  "status": "healthy",
  "version": "3.0",
  "modules": ["molecular_docking", "cell_dynamics"]
}
```

#### Run Molecular Docking
```http
POST /api/docking/run
Content-Type: application/json

{
  "proteinId": "6LU7",
  "ligandId": "remdesivir",
  "numModes": 9
}
```
**Response:**
```json
{
  "success": true,
  "data": {
    "protein": {...},
    "ligand": {...},
    "modes": [...],
    "best_affinity": -8.5,
    "binding_site": {...}
  }
}
```

#### Get Proteins
```http
GET /api/docking/proteins
```

#### Get Ligands
```http
GET /api/docking/ligands
```

#### Run Cell Simulation
```http
POST /api/cells/simulate
Content-Type: application/json

{
  "cellLineName": "HeLa",
  "experimentParams": {
    "initialCells": 50,
    "duration": 72,
    "timeInterval": 0.5
  },
  "environment": {
    "temperature": 37,
    "co2": 5,
    "humidity": 95
  },
  "treatment": {
    "type": "drug",
    "concentration": 10
  }
}
```

#### Get Cell Lines
```http
GET /api/cells/cell-lines
```

#### Predict Drug Efficacy
```http
POST /api/predict/drug-efficacy
Content-Type: application/json

{
  "cellLineName": "HeLa",
  "drugClass": "taxol",
  "concentration": 10
}
```

---

## 💡 Usage Examples

### Example 1: Complete Drug Discovery Workflow *(Pro Version)*

**Scenario:** Evaluate Remdesivir against SARS-CoV-2

1. **Molecular Docking**
   - Select: SARS-CoV-2 Mpro (6LU7)
   - Choose: Remdesivir
   - Run docking
   - Result: -9.2 kcal/mol binding affinity

2. **Efficacy Prediction**
   - Set concentration: 10 μM
   - Calculate efficacy
   - Result: 65% predicted cell kill

3. **Cell Simulation**
   - Cell line: A549 (Lung cancer)
   - Simulate 72 hours
   - Observe: Drug effects visualized in red
   - Export: Complete workflow report

### Example 2: Multi-Compound Screening

```python
# Screen multiple NSAIDs against COX-2
compounds = ['aspirin', 'ibuprofen']

for compound in compounds:
    # Dock each compound
    results = dock(protein='2OXY', ligand=compound)
    
    # Compare affinities
    print(f"{compound}: {results.best_affinity} kcal/mol")
    
    # Export for comparison
    export_csv(results)
```

### Example 3: Cell Line Comparison

Test same drug across different cell lines:
- HeLa (cervical cancer)
- MCF-7 (breast cancer)
- A549 (lung cancer)
- Compare growth inhibition
- Export data for statistical analysis

### Example 4: Educational Demo

Perfect for teaching:
1. Show molecular docking principles
2. Explain SAR (Structure-Activity Relationships)
3. Demonstrate dose-response curves
4. Visualize cellular effects in real-time
5. Discuss drug development pipeline

---

## 🛠️ Technology Stack

### Frontend
- **React 18** - UI framework
- **Recharts** - Data visualization
- **HTML5 Canvas** - Real-time cell rendering
- **CSS3** - Professional dark theme with animations

### Backend
- **Flask 3.0** - Python web framework
- **NumPy & SciPy** - Scientific computing
- **Gunicorn** - Production WSGI server
- **Flask-CORS** - Cross-origin support

### Deployment
- **Render.com** - Recommended cloud platform
- **Heroku** - Alternative cloud platform
- **Any Python 3.11 host** - Self-hosted option

---

## 📦 File Structure

```
biomed-research-suite/
├── biomed_suite_pro.html          # Pro version (v3.0) ⭐
├── unified_biomedical_suite.html  # Basic version (v2.0)
├── unified_backend.py             # Flask backend API
├── requirements.txt               # Python dependencies
├── runtime.txt                    # Python 3.11
├── Procfile                       # Heroku deployment
├── render.yaml                    # Render.com deployment
├── validate_system.py             # System validation script
├── README.md                      # This file
├── QUICKSTART.md                  # Quick start guide
└── WHATS_NEW.md                   # v3.0 changelog
```

---

## 🎯 Version Comparison

| Feature | Basic v2.0 | Pro v3.0 |
|---------|-----------|----------|
| **Workflow** | Manual tab switching | Integrated 3-step process |
| **Docking** | ✅ Standard | ✅ Enhanced with efficiency |
| **Efficacy Prediction** | ❌ | ✅ IC50 & dose-response |
| **Cell Simulation** | ✅ Standard | ✅ Drug effect visualization |
| **ADMET** | Basic | Comprehensive (5 categories) |
| **Export JSON** | ✅ | ✅ Enhanced |
| **Export CSV** | ❌ | ✅ |
| **Complete Reports** | ❌ | ✅ |
| **Animations** | Basic | Professional |
| **Progress Tracking** | ❌ | ✅ |
| **Interaction Strength** | ❌ | ✅ Weak/Moderate/Strong |
| **Use Case** | Learning & basic research | Professional research |

**Recommendation:** Start with Pro version for complete experience.

---

## ⚙️ Configuration

### Environment Variables
```bash
PORT=5000              # Server port
FLASK_ENV=production   # Environment
RENDER=true           # Render.com flag (auto-set)
DYNO=true             # Heroku flag (auto-set)
```

### CORS Settings
Backend accepts requests from:
- `localhost:*` (development)
- `127.0.0.1:*` (development)
- `*.onrender.com` (Render)
- `*.herokuapp.com` (Heroku)
- `file://` (local HTML)

### Custom Configuration
Edit `unified_backend.py`:
```python
# Add custom protein
PROTEIN_DATABASE['CUSTOM'] = ProteinProfile(
    pdb_id='XXXX',
    name='Your Protein',
    # ...
)

# Add custom ligand
LIGAND_DATABASE['custom'] = LigandProfile(
    name='Your Compound',
    # ...
)
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check Python version
python --version  # Should be 3.11

# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Check port availability
lsof -i :5000  # MacOS/Linux
netstat -ano | findstr :5000  # Windows
```

### Frontend can't connect
1. Verify backend is running: `curl http://127.0.0.1:5000/api/health`
2. Check browser console for errors
3. Ensure CORS is enabled (should be automatic)
4. Try different browser

### Simulations run slowly
- Reduce initial cell count (default: 50 → try 20)
- Decrease duration (72h → try 24h)
- Upgrade hosting plan (free tier → paid)
- Close other browser tabs

### Deployment fails
```bash
# Render.com
- Check build logs in dashboard
- Verify render.yaml is in root directory
- Ensure requirements.txt is correct

# Heroku
heroku logs --tail
heroku ps:restart
```

### Canvas not rendering
- Enable JavaScript in browser
- Update to modern browser version
- Check browser console for errors
- Try clearing cache

---

## 📊 Performance Tips

### For Local Development
```bash
# Use development server
python unified_backend.py

# Monitor performance
python -m cProfile unified_backend.py
```

### For Production
```bash
# Use more workers (adjust based on server)
gunicorn unified_backend:app --workers 4 --threads 8

# Enable caching (optional)
pip install redis
# Uncomment redis lines in requirements.txt
```

### For Large Simulations
- Start with small test runs
- Monitor memory usage
- Export data periodically
- Use batch processing for multiple runs

---

## 🎓 Educational Use

### For Students
- Learn drug discovery pipeline
- Understand molecular interactions
- Practice data analysis
- Export results for reports

### For Educators
- Live classroom demonstrations
- Homework assignments
- Research project platform
- Customizable parameters

### For Workshops
- Hands-on training
- Group exercises
- Real-time feedback
- Exportable data

---

## 🔬 Research Applications

### Drug Discovery
- Virtual screening
- Lead optimization
- ADMET filtering
- Mechanism of action studies

### Cancer Research
- Anti-cancer drug testing
- Cell line comparison
- Dose-response analysis
- Combination therapy modeling

### Computational Biology
- Structure-function relationships
- Systems biology integration
- Data-driven predictions
- Method validation

### Pharmaceutical Development
- Pre-clinical screening
- Target validation
- Toxicity assessment
- Formulation studies

---

## 🚧 Roadmap

### v4.0 (Coming Soon)
- [ ] 3D molecular visualization with Three.js
- [ ] Machine learning predictions
- [ ] Multi-compound comparison dashboard
- [ ] Custom cell line builder
- [ ] Batch processing API
- [ ] Session save/restore
- [ ] PDF report generation
- [ ] Mobile-responsive design

### v5.0 (Future)
- [ ] Real PDB structure loading
- [ ] Protein-protein docking
- [ ] QSAR modeling
- [ ] Network pharmacology
- [ ] Clinical trial simulation
- [ ] Regulatory compliance tools

---

## 🤝 Contributing

We welcome contributions!

### Areas for Improvement
- Algorithm optimization
- New visualization types
- Additional cell lines
- More drug compounds
- UI/UX enhancements
- Documentation
- Testing
- Bug fixes

### How to Contribute
1. Fork the repository
2. Create feature branch
3. Make your changes
4. Test thoroughly
5. Submit pull request

---

## 📄 License

Educational and research use.

**Not for clinical decision making or medical advice.**

This software is for educational and research purposes only. Results are computational predictions and should be validated experimentally.

---

## 💬 Support

### Documentation
- README.md (this file)
- QUICKSTART.md (fast setup)
- WHATS_NEW.md (v3.0 features)
- API docs (in this file)

### Common Issues
Check troubleshooting section above

### System Validation
```bash
python validate_system.py
```

### Export Debug Info
Use export functions to save:
- Docking results
- Simulation data
- Complete workflow reports

---

## 🎖️ Credits

**Developed for the scientific community**

Built with:
- Modern web technologies
- Open source libraries
- Scientific computing tools
- Professional design principles

**Special Thanks:**
- React team
- Flask team
- Scientific Python community
- All contributors

---

## 📞 Contact

For issues, questions, or feedback:
- Review documentation
- Run validation script
- Check troubleshooting section
- Export data for analysis

---

**BioMed Research Suite v3.0 Pro**

*Professional Integrated Drug Discovery Platform*

🧬 **From Molecules to Cells - One Seamless Workflow**

*Built for Researchers | Designed for Discovery | Optimized for Results*

---

© 2024 BioMed Research Suite | Educational Software
