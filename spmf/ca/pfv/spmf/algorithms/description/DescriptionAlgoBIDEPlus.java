package ca.pfv.spmf.algorithms.description;

import java.io.IOException;

/* This file is copyright (c) 2008-2013 Philippe Fournier-Viger
* 
* This file is part of the SPMF DATA MINING SOFTWARE
* (http://www.philippe-fournier-viger.com/spmf).
* 
* SPMF is free software: you can redistribute it and/or modify it under the
* terms of the GNU General Public License as published by the Free Software
* Foundation, either version 3 of the License, or (at your option) any later
* version.
* 
* SPMF is distributed in the hope that it will be useful, but WITHOUT ANY
* WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
* A PARTICULAR PURPOSE. See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License along with
* SPMF. If not, see <http://www.gnu.org/licenses/>.
*/
import ca.pfv.spmf.algorithms.sequentialpatterns.prefixspan.AlgoBIDEPlus;

/**
 * This class describes the BIDE+ algorithm parameters. It is designed to be used by the graphical and command line interface.
 * 
 * @see AlgoBIDEPlus
 * @author Philippe Fournier-Viger
 */
public class DescriptionAlgoBIDEPlus extends DescriptionOfAlgorithm {

	public DescriptionAlgoBIDEPlus(){
		
	}

	@Override
	String getName() {
		return "BIDE+";
	}

	@Override
	String getAlgorithmCategory() {
		return "SEQUENTIAL PATTERN MINING";
	}

	@Override
	String getURLOfDocumentation() {
		return "http://www.philippe-fournier-viger.com/spmf/index.php?link=documentation.php#exampleBIDE";
	}

	@Override
	void runAlgorithm(String[] parameters, String inputFile, String outputFile) throws IOException {

		// sequenceDatabase.print();
		double minsup = getParamAsDouble(parameters[0]); // we use a minimum support of 2
											// sequences.

		boolean outputSeqIdentifiers = false;
		if (parameters.length >=2 && "".equals(parameters[1]) == false) {
			outputSeqIdentifiers = getParamAsBoolean(parameters[1]);
		}
		
		AlgoBIDEPlus algo = new AlgoBIDEPlus();
		algo.setShowSequenceIdentifiers(outputSeqIdentifiers);
		algo.runAlgorithm(inputFile, minsup, outputFile);
		algo.printStatistics();
	}

	@Override
	DescriptionOfParameter[] getParametersDescription() {
        
		DescriptionOfParameter[] parameters = new DescriptionOfParameter[2];
		parameters[0] = new DescriptionOfParameter("minsup (%)", "(e.g. 0.4 or 40%)", Double.class, false);
		parameters[1] = new DescriptionOfParameter("Show sequence ids? (optional):", "(default: false)", Double.class, true);;
		return null;
	}

	@Override
	String getImplementationAuthorName() {
		return "Philippe Fournier-Viger";
	}
	
}
